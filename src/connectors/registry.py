"""Data-source catalogue and refresh policy for the web application."""
from __future__ import annotations

SOURCES = [
    {
        "id": "alpha_vantage_usd_inr",
        "name": "USD/INR exchange rate",
        "provider": "Alpha Vantage",
        "frequency": "Market feed; provider refresh cadence applies",
        "mode": "api",
        "key_variable": "ALPHAVANTAGE_API_KEY",
        "status_note": "Automatic refresh is available after an API key is configured.",
        "url": "https://www.alphavantage.co/documentation/",
    },
    {
        "id": "oilpriceapi_brent",
        "name": "Brent crude benchmark",
        "provider": "OilPriceAPI",
        "frequency": "Latest provider-published observation",
        "mode": "api",
        "key_variable": "OILPRICEAPI_KEY",
        "status_note": "Automatic refresh is available after an API key is configured. This is a Brent benchmark proxy, not IndiGo's realised ATF cost.",
        "url": "https://docs.oilpriceapi.com/api-reference/prices/latest",
    },
    {
        "id": "mospi_cpi",
        "name": "India CPI inflation",
        "provider": "MoSPI eSankhyiki",
        "frequency": "Monthly, on official release",
        "mode": "official_release_import",
        "key_variable": None,
        "status_note": "Import the released monthly series; it is not an intraday feed.",
        "url": "https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI",
    },
    {
        "id": "oea_wpi",
        "name": "India WPI inflation",
        "provider": "Office of the Economic Adviser",
        "frequency": "Monthly, on official release",
        "mode": "official_release_import",
        "key_variable": None,
        "status_note": "Import the official monthly index/release and retain the base-year definition.",
        "url": "https://eaindustry.nic.in/download_data_2223.asp",
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
