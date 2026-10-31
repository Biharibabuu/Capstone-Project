const API_BASE = window.INDIGO_API_BASE || "http://127.0.0.1:8000";
const apiPill = document.querySelector("#api-pill");
const modelPill = document.querySelector("#model-pill");
const healthMessage = document.querySelector("#health-message");
const modelState = document.querySelector("#model-state");
const modelDetail = document.querySelector("#model-detail");
const marketStatus = document.querySelector("#market-status");
const marketGrid = document.querySelector("#market-grid");
const sourceList = document.querySelector("#source-list");
const refreshButton = document.querySelector("#refresh-market");

function setPill(element, text, kind = "pending") {
  if (!element) return;
  element.textContent = text;
  element.className = "pill pill-" + kind;
}

function formatTimestamp(value) {
  if (!value) return "Timestamp unavailable";
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? String(value) : date.toLocaleString();
}

function renderMarketData(records) {
  if (!marketGrid) return;
  marketGrid.replaceChildren();
  if (!records || records.length === 0) {
    marketGrid.textContent = "No market observations stored yet. Add the API keys to .env and select Refresh market data.";
    return;
  }

  const names = {
    alpha_vantage_usd_inr: "USD/INR",
    oilpriceapi_brent: "Brent crude benchmark",
    mospi_cpi: "India CPI inflation",
    mospi_wpi: "India WPI inflation",
  };
  records.forEach((record) => {
    const card = document.createElement("article");
    card.className = "market-metric";
    const heading = document.createElement("h3");
    heading.textContent = names[record.source] || record.source;
    const value = document.createElement("p");
    value.className = "market-value";
    const prefix = record.currency === "INR" ? "₹" : record.currency === "USD" ? "$" : "";
    const decimals = record.source === "alpha_vantage_usd_inr" ? 4 : 2;
    value.textContent = (prefix + Number(record.value).toFixed(decimals) + " " + (record.unit || "")).trim();
    const observed = document.createElement("p");
    observed.className = "muted market-timestamp";
    observed.textContent = (record.reference_period ? "Reference period: " + record.reference_period + " · " : "") + "Observation time: " + formatTimestamp(record.observed_at) + (record.publication_date ? " · Released: " + record.publication_date : "");
    const freshness = document.createElement("span");
    freshness.className = record.freshness === "stale" ? "pill pill-error" : "pill pill-good";
    freshness.textContent = record.freshness === "stale" ? "Potentially stale" : "Latest stored observation";
    card.append(heading, value, observed, freshness);
    marketGrid.append(card);
  });
}

function renderSources(sources) {
  if (!sourceList) return;
  sourceList.replaceChildren();
  (sources || []).forEach((source) => {
    const item = document.createElement("li");
    const title = document.createElement("strong");
    title.textContent = source.name + " — " + source.provider;
    const detail = document.createElement("span");
    detail.textContent = source.frequency + ". " + source.status_note;
    const link = document.createElement("a");
    link.href = source.url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.textContent = "Official/provider source";
    item.append(title, detail, link);
    sourceList.append(item);
  });
}

async function checkApiHealth() {
  try {
    const response = await fetch(API_BASE + "/api/health", {
      headers: { Accept: "application/json" },
    });
    if (!response.ok) throw new Error("API returned HTTP " + response.status);
    const result = await response.json();
    setPill(apiPill, "API connected", "good");
    healthMessage.textContent = result.message || "API health check completed.";

    if (result.model_loaded && result.status === "ready") {
      setPill(modelPill, "Model service registered", "pending");
      modelState.textContent = "Service registered; validation must be confirmed";
      modelDetail.textContent = "Check the model version and evaluation metadata before using forecasts.";
    } else {
      setPill(modelPill, "Model not trained", "pending");
      modelState.textContent = "Not trained";
      modelDetail.textContent = "Market feeds can be tested now. Next, complete baseline comparison, chronological evaluation and model packaging.";
    }
  } catch (error) {
    setPill(apiPill, "API unavailable", "error");
    setPill(modelPill, "Model status unknown", "pending");
    healthMessage.textContent =
      "Start the API with 'uvicorn backend.main:app --reload' from the repository root. Details: " + error.message;
  }
}

async function loadMarketData() {
  if (marketStatus) marketStatus.textContent = "Loading latest stored observations…";
  try {
    const response = await fetch(API_BASE + "/api/market/latest", { headers: { Accept: "application/json" } });
    if (!response.ok) throw new Error("API returned HTTP " + response.status);
    const result = await response.json();
    renderMarketData(result.market_data);
    renderSources(result.sources);
    if (marketStatus) marketStatus.textContent = "Snapshot checked: " + formatTimestamp(result.as_of) + ". Values retain their source timestamps.";
  } catch (error) {
    if (marketStatus) marketStatus.textContent = "Market-data endpoint unavailable: " + error.message;
  }
}

async function refreshMarketData() {
  if (!refreshButton) return;
  refreshButton.disabled = true;
  refreshButton.textContent = "Refreshing…";
  if (marketStatus) marketStatus.textContent = "Requesting USD/INR, Brent, CPI and WPI updates…";
  try {
    const response = await fetch(API_BASE + "/api/market/refresh", { method: "POST" });
    if (!response.ok) throw new Error("API returned HTTP " + response.status);
    const result = await response.json();
    renderMarketData(result.snapshot?.market_data || []);
    renderSources(result.snapshot?.sources || []);
    const messages = (result.results || []).map((item) => item.source + ": " + item.status + (item.message ? " — " + item.message : ""));
    if (marketStatus) marketStatus.textContent = result.status + ". " + messages.join(" | ");
  } catch (error) {
    if (marketStatus) marketStatus.textContent = "Refresh failed: " + error.message;
  } finally {
    refreshButton.disabled = false;
    refreshButton.textContent = "Refresh market data";
  }
}

if (refreshButton) refreshButton.addEventListener("click", refreshMarketData);
checkApiHealth();
loadMarketData();
