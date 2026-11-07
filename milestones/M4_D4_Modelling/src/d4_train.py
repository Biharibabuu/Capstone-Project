"""D4-v1: reproducible time-aware PAT-margin regression experiment."""
from __future__ import annotations
import argparse, hashlib, itertools, json
from datetime import date
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

_FILE = Path(__file__).resolve()
ROOT = next((parent for parent in _FILE.parents if (parent / ".gitignore").exists()), _FILE.parents[1])
SEED = 42
TARGET = "pat_margin_pct"
FEATURES = ["lag1_pat_margin_pct", "lag1_ebitda_margin_pct", "lag1_usd_inr_q_mean",
            "lag1_cpi_inflation_q_mean", "lag1_wpi_inflation_q_mean", "lag1_brent_monthly_q_mean"]
SPLITS = {"train": ("2017Q4", "2022Q4"), "validation": ("2023Q1", "2024Q2"), "test": ("2024Q3", "2026Q2")}
COLS = {"PAT Margin": TARGET, "EBITDA Margin": "ebitda_margin_pct",
        "USD INR (Quarterly Mean)": "usd_inr_q_mean",
        "CPI inflation (Quarterly Mean)": "cpi_inflation_q_mean",
        "WPI inflation (Quarterly Mean)": "wpi_inflation_q_mean",
        "Oil benchmark(MONTHLY) (Quarterly Mean)": "brent_monthly_q_mean"}

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def load_data(path: Path) -> pd.DataFrame:
    if path.suffix.lower()==".csv": return pd.read_csv(path)
    return pd.read_excel(path, sheet_name="Final_Quarterly_Data")

def make_supervised(raw: pd.DataFrame) -> pd.DataFrame:
    required={"Year","Quarter (Calendar)","Financial Data Status",*COLS}
    missing=required-set(raw.columns)
    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")
    d=raw.copy()
    d["Year"]=pd.to_numeric(d["Year"],errors="coerce")
    d["q"]=pd.to_numeric(d["Quarter (Calendar)"].astype(str).str.extract(r"Q([1-4])",expand=False),errors="coerce")
    if d[["Year","q"]].isna().any().any(): raise ValueError("Invalid calendar quarter key")
    d["Year"]=d["Year"].astype(int); d["q"]=d["q"].astype(int)
    d["quarter_id"]=d["Year"].astype(str)+"Q"+d["q"].astype(str)
    d["ordinal"]=d["Year"]*4+d["q"]-1
    d=d[d["Financial Data Status"].astype(str).str.strip().eq("Reported (original value)")].copy()
    if d["quarter_id"].duplicated().any(): raise ValueError("Duplicate reported quarters")
    for col,new in COLS.items(): d[new]=pd.to_numeric(d[col],errors="coerce")
    d=d.sort_values("ordinal").reset_index(drop=True)
    rows=[]
    for i in range(1,len(d)):
        prev,cur=d.iloc[i-1],d.iloc[i]
        if int(cur["ordinal"]-prev["ordinal"])!=1: continue
        r={"target_quarter":cur["quarter_id"],"forecast_origin_quarter":prev["quarter_id"],TARGET:float(cur[TARGET])}
        r.update({f"lag1_{v}":float(prev[v]) for v in COLS.values()})
        rows.append(r)
    out=pd.DataFrame(rows)
    if out.empty or out[FEATURES+[TARGET]].isna().any().any(): raise ValueError("No complete lagged examples")
    return out

def split(d: pd.DataFrame) -> dict[str,pd.DataFrame]:
    result={k:d[d.target_quarter.between(a,b)].copy() for k,(a,b) in SPLITS.items()}
    if any(v.empty for v in result.values()): raise ValueError("Fixed split has an empty window")
    if sum(map(len,result.values()))!=len(d): raise ValueError("A supervised row falls outside the declared windows")
    if not (result['train'].target_quarter.max()<result['validation'].target_quarter.min()<result['test'].target_quarter.min()):
        raise ValueError("Split chronology is invalid")
    return result

def metrics(y,p): return {"mae":float(mean_absolute_error(y,p)),"rmse":float(np.sqrt(mean_squared_error(y,p)))}
def ridge(alpha): return Pipeline([("imputer",SimpleImputer(strategy="median")),("scale",StandardScaler()),("model",Ridge(alpha=alpha))])
def forest(depth,leaf): return Pipeline([("imputer",SimpleImputer(strategy="median")),("model",RandomForestRegressor(n_estimators=300,max_depth=depth,min_samples_leaf=leaf,max_features=1.0,random_state=SEED,n_jobs=1))])

def run(input_path: Path, outdir: Path):
    d=make_supervised(load_data(input_path)); parts=split(d); tr,va,te=parts['train'],parts['validation'],parts['test']
    digest=sha256(input_path); today=date.today().isoformat(); feature_string=";".join(FEATURES); rows=[]
    base=metrics(va[TARGET],va.lag1_pat_margin_pct)
    def log(run_id,algorithm,params,which,score,selection):
        rows.append({"run_id":run_id,"run_date":today,"data_version_sha256":digest,"dataset":input_path.name,
          "target":TARGET,"algorithm":algorithm,"parameters":json.dumps(params,sort_keys=True),"random_seed":SEED,
          "features":feature_string,"split":which,"n_train":len(tr),"n_validation":len(va),"n_test":len(te),
          "mae":score['mae'],"rmse":score['rmse'],"selection":selection})
    log("D4-BASE-01","Persistence baseline",{"prediction":"lag1_pat_margin_pct"},"validation",base,"baseline reference")
    trials=[]
    for alpha in [0.1,1.0,10.0,100.0]:
        m=ridge(alpha); m.fit(tr[FEATURES],tr[TARGET]); s=metrics(va[TARGET],m.predict(va[FEATURES])); p={"alpha":alpha}
        trials.append({"algorithm":"Ridge Regression","params":p,"score":s})
        log(f"D4-RIDGE-A{alpha:g}","Ridge Regression",p,"validation",s,"validation candidate")
    for depth,leaf in itertools.product([2,3,4],[2,3]):
        m=forest(depth,leaf); m.fit(tr[FEATURES],tr[TARGET]); s=metrics(va[TARGET],m.predict(va[FEATURES]))
        p={"n_estimators":300,"max_depth":depth,"min_samples_leaf":leaf,"max_features":1.0,"random_state":SEED}
        trials.append({"algorithm":"Random Forest","params":p,"score":s})
        log(f"D4-RF-D{depth}-L{leaf}","Random Forest",p,"validation",s,"validation candidate")
    best=min(trials,key=lambda x:(x['score']['mae'],x['score']['rmse']))
    selected=best['algorithm'] if best['score']['mae']<base['mae'] else "Persistence baseline"
    params=best['params'] if selected!="Persistence baseline" else {"prediction":"lag1_pat_margin_pct"}
    baseline_test=metrics(te[TARGET],te.lag1_pat_margin_pct)
    if selected=="Persistence baseline": pred=te.lag1_pat_margin_pct.to_numpy()
    else:
        full=pd.concat([tr,va],ignore_index=True)
        model=ridge(params['alpha']) if selected=="Ridge Regression" else forest(params['max_depth'],params['min_samples_leaf'])
        model.fit(full[FEATURES],full[TARGET]); pred=model.predict(te[FEATURES])
        (ROOT/'models').mkdir(exist_ok=True); joblib.dump({"model":model,"features":FEATURES,"target":TARGET,"seed":SEED},ROOT/'models/d4_v1_model.joblib')
    final=metrics(te[TARGET],pred)
    log("D4-FINAL-TEST-01",selected,params,"test (locked holdout; model choice fixed)",final,"final holdout score; no further tuning")
    outdir.mkdir(parents=True,exist_ok=True); pd.DataFrame(rows).to_csv(outdir/'D4_experiment_log.csv',index=False)
    predout=te[["target_quarter","forecast_origin_quarter",TARGET]].copy(); predout['prediction']=pred; predout['absolute_error']=(predout[TARGET]-predout.prediction).abs(); predout.to_csv(outdir/'D4_test_predictions.csv',index=False)
    result={"experiment_version":"d4-v1","run_date":today,"source_dataset":input_path.name,"source_dataset_sha256":digest,
      "problem_type":"supervised regression; one-quarter-ahead PAT-margin forecasting","target":TARGET,"features":FEATURES,"random_seed":SEED,
      "split_windows":SPLITS,"sample_counts":{k:len(v) for k,v in parts.items()},"sample_range":{"first":d.target_quarter.min(),"last":d.target_quarter.max()},
      "baseline_validation":base,"candidate_validation":[{"algorithm":x['algorithm'],"parameters":x['params'],**x['score']} for x in trials],
      "selected_algorithm":selected,"selected_parameters":params,"selected_validation_mae":base['mae'] if selected=="Persistence baseline" else best['score']['mae'],
      "baseline_test":baseline_test,"selected_test":final,"test_mae_improvement_vs_baseline_pct":(baseline_test['mae']-final['mae'])/baseline_test['mae']*100 if baseline_test['mae'] else 0,
      "model_artifact":None if selected=="Persistence baseline" else "models/d4_v1_model.joblib",
      "limitations":["Calendar-quarter labels are retained as supplied.","Rows marked Not available in source were excluded; lagged features use only the immediately preceding reported quarter.","Historical publication timestamps are absent; lagging limits target-quarter leakage but does not prove point-in-time availability.","Brent is a benchmark proxy, not realised ATF cost.","Small sample and extreme loss quarters limit reliability."]}
    (outdir/'D4_metrics.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    return result

# Public aliases retained for the notebook and test suite.
SPLIT_WINDOWS = SPLITS
prepare_supervised_data = make_supervised
split_data = split
run_experiment = run

def main():
    p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,default=ROOT/'data/processed/Final_Quarterly_Data(1).xlsx'); p.add_argument('--output-dir',type=Path,default=ROOT/'milestones'/'M4_D4_Modelling'/'experiments'); a=p.parse_args()
    print(json.dumps(run(a.input.resolve(),a.output_dir.resolve()),indent=2))
if __name__=='__main__': main()
