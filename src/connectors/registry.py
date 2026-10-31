"""Data-source catalogue and refresh policy for the web application."""
from __future__ import annotations

SOURCES = [
    {
        "id": "alpha_vantage_usd_inr",
        "name": "USD/INR exchange rate",
        "provider": "Alpha Vantage",
        "frequency": "Latest provider-reported FX rate; provider cadence applies",
        "mode": "api",
        "key_variable": "ALPHAVANTAGE_API_KEY",
        "status_note": "Server-side API refresh. This is a provider-reported exchange-rate observation, not a guaranteed exchange execution quote.",
        "url": "https://www.alphavantage.co/documentation/",
    },
    {
        "id": "oilpriceapi_brent",
        "name": "Brent crude benchmark",
        "provider": "OilPriceAPI",
        "frequency": "Latest provider-published observation",
        "mode": "api",
        "key_variable": "OILPRICEAPI_KEY",
        "status_note": "Server-side API refresh. Brent is a global crude benchmark proxy, not Indian ATF or IndiGo's realised fuel cost.",
        "url": "https://docs.oilpriceapi.com/api-reference/prices/latest",
    },
    {
        "id": "mospi_cpi",
        "name": "India CPI inflation",
        "provider": "MoSPI eSankhyiki",
        "frequency": "Monthly, when the official CPI release is published",
        "mode": "api",
        "key_variable": "MOSPI_API_TOKEN",
        "status_note": "Queries the All-India General Combined CPI series (2012 base year by default to avoid a documented 2024-endpoint issue). The optional Bearer token is read server-side; the API result is monthly, not intraday.",
        "url": "https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api",
    },
    {
        "id": "mospi_wpi",
        "name": "India WPI inflation",
        "provider": "MoSPI eSankhyiki / Office of the Economic Adviser",
        "frequency": "Monthly, when the official WPI release is published",
        "mode": "api",
        "key_variable": "MOSPI_API_TOKEN",
        "status_note": "Queries the All Commodities WPI series and calculates year-on-year inflation from the index if the API does not provide it directly. Base year is configurable.",
        "url": "https://esankhyiki.mospi.gov.in/macroindicators?product=wpi&tab=api",
    },
    {
        "id": "indigo_financials",
        "name": "IndiGo quarterly financial results",
        "provider": "IndiGo Investor Relations",
        "frequency": "Quarterly, after results publication",
        "mode": "official_release_import",
        "key_variable": None,
        "status_note": "Import published results; do not infer unpublished current-quarter PAT or revenue.",
        "url": "https://www.goindigo.in/information/investor-relations/quarterly-financial-results.html",
    },
]


def get_source_catalogue() -> list[dict]:
    return [dict(source) for source in SOURCES]
