# Live Data Integration — First Implementation

## Connected market APIs

| Series | Provider | Endpoint / Function | Authentication | Data meaning |
|---|---|---|---|---|
| USD/INR | Alpha Vantage | **CURRENCY_EXCHANGE_RATE**, USD to INR | **ALPHAVANTAGE_API_KEY** | Provider-reported current exchange rate and refresh timestamp |
| Brent crude | OilPriceAPI | **GET /v1/prices/latest?by_code=BRENT_CRUDE_USD** | **OILPRICEAPI_KEY** in the Authorization: Token header | Latest provider-published Brent benchmark quote, with source timestamp |

The application stores each normalized observation in a local SQLite database. A provider failure is reported independently and does not erase the last successful cached observation. A cached observation older than 72 hours is labelled **stale**; this is a dashboard warning, not a claim that the provider is publishing a quote every 72 hours.

## Official-release inputs

The source catalogue also lists CPI (MoSPI), WPI (Office of the Economic Adviser), and IndiGo quarterly financial results. These are monthly or quarterly official publications, not intraday feeds. This implementation identifies their official source pages and marks them as **official_release_import**; a stable public REST endpoint is not assumed. The next ingestion step should download/parse a published release, preserve its reference period and release date, and append it to the existing master data.

- CPI: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI
- WPI: https://eaindustry.nic.in/download_data_2223.asp
- IndiGo results: https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html

## Setup

1. Create API keys with [Alpha Vantage](https://www.alphavantage.co/documentation/) and [OilPriceAPI](https://www.oilpriceapi.com/dashboard).
2. Copy **.env.example** to **.env** and replace the placeholder values. Do not put keys in frontend JavaScript or commit **.env**.
3. Install dependencies: **pip install -r requirements.txt**.
4. Start the backend from the repository root: **uvicorn backend.main:app --reload**.
5. Open **http://127.0.0.1:8000/docs** and call **POST /api/market/refresh**.
6. Read cached values using **GET /api/market/latest**; the frontend also displays them and provides a refresh button.

## API routes

- **GET /api/market/latest** — last successfully stored values and source catalogue.
- **POST /api/market/refresh** — refresh USD/INR and Brent independently.
- **GET /api/sources** — source catalogue, cadence, source link, and ingestion mode.

## Important modelling controls

- Keep provider observation time and application fetch time separately.
- Do not treat the Brent proxy as Indian ATF or IndiGo's realised fuel expense.
- Do not call CPI/WPI real-time; update those series only when official monthly releases are published.
- Do not use unpublished financial outcomes as live predictors. IndiGo revenue/PAT are imported after quarterly results are published.
- Build historical training features using the same calculation definitions as the live feature-refresh pipeline. A current spot quote must not be substituted for a historical quarterly average without changing and evaluating the model feature definition.
- API keys and provider responses must remain server-side. Check each provider's current rate limits, data-use and display/redistribution terms before any public deployment.
