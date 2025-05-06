# VELO Python SDK

The VELO Python SDK provides a streamlined interface for interacting with the VELO API, enabling businesses to access and analyze climate risk data for companies, assets, and market indexes.

For complete API documentation visit our [API docs](https://api.docs.riskthinking.ai).

## Installation

```bash
pip install velo-sdk
```

## Requirements

- Python 3.11 or higher

## Authentication

The SDK requires an API key for authentication. You can pass your API key when initializing the client:

```python
from velo_sdk.api import APIClient

client = APIClient(api_key="your-api-key")
```

If the `api_key` parameter is not provided, the API key will be inferred from the `RISKTHINKING_API_KEY` environment variable instead.

## Features

### Companies

Access company data including associated assets and market information:

```python
# Get specific company data
company = client.companies.get_company("company-id")

# List companies with pagination
for company in client.companies.list_companies():
    print(company.name)

# Search for companies by name
results = client.companies.search_companies(name="Company Name")

# List assets owned by a company
for asset in client.companies.list_company_assets("company-id"):
    print(asset.name)

# Get climate scores for a company
scores = client.companies.get_company_climate_scores(
    "company-id", 
    pathway="SV", 
    horizon=2050
)

# Get impact scores aggregated by country
for country_score in client.companies.aggregate_company_asset_climate_scores_by_country(
    "company-id", 
    pathway="SV", 
    horizon=2050
):
    print(f"{country_score.country}: {country_score.dcr_score}")
```

### Assets

Retrieve and analyze physical assets and their climate risk scores:

```python
# Get asset details
asset = client.assets.get_asset("asset-id")

# List all assets with pagination
for asset in client.assets.list_assets():
    print(f"{asset.name} ({asset.asset_type})")

# Get the owner of an asset
owner = client.assets.get_asset_owner("asset-id")
```

### Market Indexes

Access market indexes and associated climate risk analytics:

```python
# List available market indexes
for index in client.markets.list_indexes():
    print(index.name)

# Get companies in a specific index
for company in client.markets.get_index_companies("index-id"):
    print(company.name)

# Get climate scores for an index
scores = client.markets.get_index_climate_scores(
    "index-id", 
    pathway="SV", 
    horizon=2050
)

# Get impact scores aggregated by country
for country_score in client.markets.aggregate_index_asset_climate_scores_by_country(
    "index-id", 
    pathway="SV", 
    horizon=2050
):
    print(f"{country_score.country}: {country_score.dcr_score}")
```

### Direct API Access

For advanced use cases, you can make direct HTTP requests to any endpoint while still using your authentication credentials:

```python
# Make a GET request with query parameters
response = client.get("/custom/endpoint", params={"param1": "value1"})

# Make a POST request with JSON body
response = client.post(
    "/custom/endpoint", 
    json={"key": "value"}
)

# Async API calls are also supported
async def make_request():
    response = await client.get_async("/custom/endpoint")
    print(response)
```

These methods (get, post, put, delete) and their async variants allow you to interact with any API endpoint not explicitly covered by the SDK's high-level methods.

## Async Support

The SDK provides async versions of all API methods:

```python
import asyncio
from velo_sdk.api import APIClient

async def main():
    client = APIClient(api_key="your-api-key")
    company = await client.companies.get_company_async("company-id")
    print(company.name)

asyncio.run(main())
```

## Pagination

The SDK handles pagination automatically for list endpoints:

```python
# Iterate through all results (automatically handles pagination)
for company in client.companies.list_companies():
    print(company.name)
```

## Error Handling

The SDK provides clear error messages for API errors:

```python
from velo_sdk.api import APIError

try:
    company = client.companies.get_company("non-existent-id")
except APIError as e:
    print(f"Error: {e.status_code} - {e.message}")
```


## Support

For questions or support, please contact velo@riskthinking.ai.

