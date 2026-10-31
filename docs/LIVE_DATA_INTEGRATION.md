# Live Data Integration — Four External Data Connectors

The web application no longer requires a Bloomberg Terminal session. Four server-side connectors refresh the market and macro inputs used by the IndiGo profitability project.

## Connected inputs

| Input | Provider | Endpoint / method | Credential | Frequency and definition |
|---|---|---|---|---|
| USD/INR | Alpha Vantage | `CURRENCY_EXCHANGE_RATE`, USD to INR | `ALPHAVANTAGE_API_KEY` | Latest provider-reported FX observation; see provider cadence and plan limits |
| Brent crude | OilPriceAPI | `GET /v1/prices/latest?by_code=BRENT_CRUDE_USD` | `OILPRICEAPI_KEY` | Latest provider-published Brent benchmark quote |
| CPI inflation | MoSPI eSankhyiki | `/api/cpi/getCPIIndex` for base year 2012 by default | Optional `MOSPI_API_TOKEN` Bearer token | Monthly All-India General Combined CPI inflation |
| WPI inflation | MoSPI eSankhyiki | `/api/wpi/getWpiRecords` | Optional `MOSPI_API_TOKEN` Bearer token | Monthly All Commodities WPI; year-on-year change is calculated from index values when no inflation field is supplied |

The CPI and WPI API parameter choices are based on the official MoSPI OpenAPI specifications and the NSO's published eSankhyiki API client examples. CPI defaults to the 2012 series through `getCPIIndex`; the NSO changelog notes an upstream 400 regression for the 2024 endpoint in its integration tests. The connector selects All-India General Combined. You can test the 2024 series by setting `MOSPI_CPI_BASE_YEAR=2012` once the endpoint is confirmed working. The WPI connector defaults to the newer 2022-23 base year and selects the All Commodities aggregate. Change the base years only after checking the matching series and definitions.

Official references:
- CPI API: https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api
- WPI API: https://esankhyiki.mospi.gov.in/macroindicators?product=wpi&tab=api
- CPI specification: https://raw.githubusercontent.com/nso-india/esankhyiki-mcp/main/swagger/swagger_user_cpi.yaml
- WPI specification: https://raw.githubusercontent.com/nso-india/esankhyiki-mcp/main/swagger/swagger_user_wpi.yaml
- NSO API client examples: https://github.com/nso-india/mospi-esankhyiki
- Alpha Vantage: https://www.alphavantage.co/documentation/
- OilPriceAPI: https://docs.oilpriceapi.com/api-reference/prices/latest

## Data meaning and cadence

- USD/INR and Brent are market observations. The provider timestamp is stored separately from the time this application fetched the data.
- CPI and WPI are monthly official statistics, not intraday market feeds. The latest available month may lag the current calendar month until the next release is published.
- CPI is stored as All-India General Combined year-on-year inflation. The default base year is 2012 for endpoint compatibility; the 2024 base-year route remains configurable. If the API supplies an index but not a percentage, the connector derives year-on-year inflation only when the same month in the prior year is available in the same base-year series.
- WPI is stored as All Commodities year-on-year inflation. If only the index is supplied, the connector calculates `(current index / index 12 months earlier - 1) × 100`. It will fail safely rather than substitute a subgroup when the All Commodities aggregate is missing.
- Brent crude is a global benchmark proxy, not Indian aviation turbine fuel (ATF) and not IndiGo's realised fuel cost.
- IndiGo revenue and PAT remain quarterly published financial outcomes. They must be imported only after public release.

## Setup

1. Get an Alpha Vantage key: https://www.alphavantage.co/support/#api-key
2. Create an OilPriceAPI account and obtain a key: https://www.oilpriceapi.com/dashboard
3. Copy `.env.example` to `.env` and enter the two provider keys. The MoSPI Bearer token is optional for open endpoints; if MoSPI responds with HTTP 401/403, configure `MOSPI_API_TOKEN` using an authorized token issued through the portal's API access process.
4. Install dependencies: `pip install -r requirements.txt`.
5. Start the backend from the repository root: `uvicorn backend.main:app --reload`.
6. Open `http://127.0.0.1:8000/docs` and call `POST /api/market/refresh`.
7. Read the latest cached observations using `GET /api/market/latest`.

Never put API credentials in browser JavaScript or commit the real `.env` file to GitHub. The backend stores the last successful observation in a local SQLite cache. A provider failure does not delete a previous successful value.

## API routes

- `GET /api/market/latest` — latest stored USD/INR, Brent, CPI and WPI records, including source timestamps and freshness status.
- `POST /api/market/refresh` — attempts all four connectors independently; partial success is reported per source.
- `GET /api/sources` — source catalogue, cadence, official/provider links and connection mode.

The current refresh action is user-triggered. A hosted deployment can later add a scheduler, with a slower cadence for CPI/WPI than for market quotes.

## Model and point-in-time safeguards

- Keep provider observation time, reference month, publication date (when supplied), and application fetch time separate.
- Do not use a current spot FX or Brent price as a historical quarterly average. The training and prediction pipelines must calculate matching features.
- Use the CPI/WPI observation only after its publication date is on or before the forecast cutoff. If publication dates are unavailable, record this limitation and use a conservative release-lag rule; do not pretend the reference month's end is the release date.
- CPI/WPI base-year revisions can change index levels. Inflation rates can be compared only when the correct matching series and calculation method are used. Do not splice index levels from different base years.
- Check provider quotas, terms, and display/redistribution rights before public deployment. OilPriceAPI's terms may restrict public display or redistribution of raw price data.
- Keep last-good-value caching and visible freshness warnings. Do not forecast when required values are missing or beyond the configured freshness window.
