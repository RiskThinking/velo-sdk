<a id="velo_sdk.api"></a>

# velo\_sdk.api

<a id="velo_sdk.api.base"></a>

# velo\_sdk.api.base

<a id="velo_sdk.api.base.BaseClient"></a>

## BaseClient Objects

```python
class BaseClient()
```

<a id="velo_sdk.api.base.BaseClient.get"></a>

#### get

```python
def get(path: str, params: Dict[str, Any] = dict(),
        **kwargs) -> Dict[str, Any]
```

Make a GET request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `params` - Query parameters
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.base.BaseClient.get_async"></a>

#### get\_async

```python
async def get_async(path: str, params: Dict[str, Any] = dict(),
                    **kwargs) -> Dict[str, Any]
```

Make an asynchronous GET request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `params` - Query parameters
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.base.BaseClient.post"></a>

#### post

```python
def post(path: str, json: Dict[str, Any] = dict(), **kwargs) -> Dict[str, Any]
```

Make a POST request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `json` - JSON body data
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.base.BaseClient.post_async"></a>

#### post\_async

```python
async def post_async(path: str, json: Dict[str, Any] = dict(),
                     **kwargs) -> Dict[str, Any]
```

Make an asynchronous POST request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `json` - JSON body data
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.base.BaseClient.put"></a>

#### put

```python
def put(path: str, json: Dict[str, Any] = dict(), **kwargs) -> Dict[str, Any]
```

Make a PUT request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `json` - JSON body data
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.base.BaseClient.put_async"></a>

#### put\_async

```python
async def put_async(path: str, json: Dict[str, Any] = dict(),
                    **kwargs) -> Dict[str, Any]
```

Make an asynchronous PUT request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `json` - JSON body data
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.base.BaseClient.delete"></a>

#### delete

```python
def delete(path: str, **kwargs) -> Dict[str, Any]
```

Make a DELETE request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.base.BaseClient.delete_async"></a>

#### delete\_async

```python
async def delete_async(path: str, **kwargs) -> Dict[str, Any]
```

Make an asynchronous DELETE request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.base.BaseClient.patch"></a>

#### patch

```python
def patch(path: str, json: Dict[str, Any] = dict(),
          **kwargs) -> Dict[str, Any]
```

Make a PATCH request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `json` - JSON body data
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.base.BaseClient.patch_async"></a>

#### patch\_async

```python
async def patch_async(path: str, json: Dict[str, Any] = dict(),
                      **kwargs) -> Dict[str, Any]
```

Make an asynchronous PATCH request to the API.
The version /v3 is automatically added to the path.

**Arguments**:

- `path` - API endpoint path
- `json` - JSON body data
- `**kwargs` - Additional arguments to pass to the request
  

**Returns**:

  API response data as JSON deserialized into a dictionary

<a id="velo_sdk.api.api_client"></a>

# velo\_sdk.api.api\_client

<a id="velo_sdk.api.pagination"></a>

# velo\_sdk.api.pagination

<a id="velo_sdk.api.pagination.PaginatedIterator"></a>

## PaginatedIterator Objects

```python
class PaginatedIterator(Generic[T], Iterator[T])
```

<a id="velo_sdk.api.pagination.PaginatedIterator.fetch_page"></a>

#### fetch\_page

```python
def fetch_page() -> list[T]
```

Fetches the next page of results and returns them as a list.

<a id="velo_sdk.api.pagination.AsyncPaginatedIterator"></a>

## AsyncPaginatedIterator Objects

```python
class AsyncPaginatedIterator(Generic[T], AsyncIterator[T])
```

<a id="velo_sdk.api.pagination.AsyncPaginatedIterator.afetch_page"></a>

#### afetch\_page

```python
async def afetch_page() -> list[T]
```

Asynchronously fetches the next page of results and returns them as a list.

<a id="velo_sdk.api.errors"></a>

# velo\_sdk.api.errors

<a id="velo_sdk.api.errors.APIError"></a>

## APIError Objects

```python
class APIError(Exception)
```

General exception for API errors.

**Attributes**:

- `message` - The error message.
- `code` - HTTP status code.
- `status` - HTTP status text.
- `timestamp` - When the error occurred.

<a id="velo_sdk.api.errors.RateLimitError"></a>

## RateLimitError Objects

```python
class RateLimitError(APIError)
```

Exception raised when rate limiting is exceeded.

<a id="velo_sdk.api.types"></a>

# velo\_sdk.api.types

<a id="velo_sdk.api.types.Company"></a>

## Company Objects

```python
class Company(BaseModel)
```

A company is an entity that has assets and identifying information.

<a id="velo_sdk.api.types.Asset"></a>

## Asset Objects

```python
class Asset(BaseModel)
```

An asset represents aphysical asset that is subject to climate risk.

<a id="velo_sdk.api.types.MarketIndex"></a>

## MarketIndex Objects

```python
class MarketIndex(BaseModel)
```

A market index is a collection of companies.

<a id="velo_sdk.api.types.ClimateScore"></a>

## ClimateScore Objects

```python
class ClimateScore(BaseModel)
```

The cimate risk metrics that represent the likelihood of a company or asset to be impacted by climate risk.

<a id="velo_sdk.api.types.ImpactScore"></a>

## ImpactScore Objects

```python
class ImpactScore(BaseModel)
```

The impact risk metrics that represent the potential impact of a company or asset to be impacted by climate risk.
These metrics represent an individual risk factor and its attribution to the total climate risk metrics.

<a id="velo_sdk.api.types.CountryClimateScore"></a>

## CountryClimateScore Objects

```python
class CountryClimateScore(ClimateScore)
```

Climate risk metrics aggregated for a country.

<a id="velo_sdk.api.types.CountryImpactScore"></a>

## CountryImpactScore Objects

```python
class CountryImpactScore(ImpactScore)
```

Impact risk metrics aggregated for a country.

<a id="velo_sdk.api.types.AssetTypeClimateScore"></a>

## AssetTypeClimateScore Objects

```python
class AssetTypeClimateScore(ClimateScore)
```

Climate risk metrics aggregated for an asset type.

<a id="velo_sdk.api.types.AssetTypeImpactScore"></a>

## AssetTypeImpactScore Objects

```python
class AssetTypeImpactScore(ImpactScore)
```

Impact risk metrics aggregated for an asset type.

<a id="velo_sdk.api.types.AssetClimateScore"></a>

## AssetClimateScore Objects

```python
class AssetClimateScore(ClimateScore)
```

Climate risk metrics for an asset.

<a id="velo_sdk.api.types.AssetImpactScore"></a>

## AssetImpactScore Objects

```python
class AssetImpactScore(BaseModel)
```

Impact risk metrics for an asset.

<a id="velo_sdk.api.markets"></a>

# velo\_sdk.api.markets

<a id="velo_sdk.api.markets.Markets"></a>

## Markets Objects

```python
class Markets()
```

<a id="velo_sdk.api.markets.Markets.search_indexes"></a>

#### search\_indexes

```python
def search_indexes(*,
                   name: Optional[str] = None,
                   **extra_params: Any) -> list[MarketIndex]
```

Search for market indexes by name.

<a id="velo_sdk.api.markets.Markets.search_indexes_async"></a>

#### search\_indexes\_async

```python
async def search_indexes_async(*,
                               name: Optional[str] = None,
                               **extra_params: Any) -> list[MarketIndex]
```

Search for market indexes by name asynchronously.

<a id="velo_sdk.api.markets.Markets.list_indexes"></a>

#### list\_indexes

```python
def list_indexes() -> PaginatedIterator[MarketIndex]
```

List all market indexes.

<a id="velo_sdk.api.markets.Markets.list_indexes_async"></a>

#### list\_indexes\_async

```python
async def list_indexes_async() -> AsyncPaginatedIterator[MarketIndex]
```

List all market indexes asynchronously.

<a id="velo_sdk.api.markets.Markets.get_index"></a>

#### get\_index

```python
def get_index(index_id: str) -> MarketIndex
```

Get a market index by its unique ID.

<a id="velo_sdk.api.markets.Markets.get_index_async"></a>

#### get\_index\_async

```python
async def get_index_async(index_id: str) -> MarketIndex
```

Get a market index by its unique ID asynchronously.

<a id="velo_sdk.api.markets.Markets.get_index_companies"></a>

#### get\_index\_companies

```python
def get_index_companies(index_id: str) -> PaginatedIterator[Company]
```

Get all companies in a market index.

<a id="velo_sdk.api.markets.Markets.get_index_companies_async"></a>

#### get\_index\_companies\_async

```python
async def get_index_companies_async(
        index_id: str) -> AsyncPaginatedIterator[Company]
```

Get all companies in a market index asynchronously.

<a id="velo_sdk.api.markets.Markets.get_index_climate_scores"></a>

#### get\_index\_climate\_scores

```python
def get_index_climate_scores(index_id: str, pathway: str,
                             horizon: int) -> ClimateScore
```

Get the climate scores for a market index.

<a id="velo_sdk.api.markets.Markets.get_index_climate_scores_async"></a>

#### get\_index\_climate\_scores\_async

```python
async def get_index_climate_scores_async(index_id: str, pathway: str,
                                         horizon: int) -> ClimateScore
```

Get the climate scores for a market index asynchronously.

<a id="velo_sdk.api.markets.Markets.get_index_impact_scores"></a>

#### get\_index\_impact\_scores

```python
def get_index_impact_scores(index_id: str, pathway: str,
                            horizon: int) -> StaticListIterator[ImpactScore]
```

Get the impact scores for a market index.

<a id="velo_sdk.api.markets.Markets.get_index_impact_scores_async"></a>

#### get\_index\_impact\_scores\_async

```python
async def get_index_impact_scores_async(
        index_id: str, pathway: str,
        horizon: int) -> StaticListIterator[ImpactScore]
```

Get the impact scores for a market index asynchronously.

<a id="velo_sdk.api.markets.Markets.aggregate_index_asset_climate_scores_by_country"></a>

#### aggregate\_index\_asset\_climate\_scores\_by\_country

```python
def aggregate_index_asset_climate_scores_by_country(
        index_id: str, pathway: str,
        horizon: int) -> StaticListIterator[CountryClimateScore]
```

Get the climate scores for all assets in a market index aggregated by country.

<a id="velo_sdk.api.markets.Markets.aggregate_index_asset_climate_scores_by_country_async"></a>

#### aggregate\_index\_asset\_climate\_scores\_by\_country\_async

```python
async def aggregate_index_asset_climate_scores_by_country_async(
        index_id: str, pathway: str,
        horizon: int) -> StaticListIterator[CountryClimateScore]
```

Get the climate scores for all assets in a market index aggregated by country asynchronously.

<a id="velo_sdk.api.markets.Markets.aggregate_index_asset_impact_scores_by_country"></a>

#### aggregate\_index\_asset\_impact\_scores\_by\_country

```python
def aggregate_index_asset_impact_scores_by_country(
        index_id: str, pathway: str,
        horizon: int) -> StaticListIterator[CountryImpactScore]
```

Get the impact scores for all assets in a market index aggregated by country.

<a id="velo_sdk.api.markets.Markets.aggregate_index_asset_impact_scores_by_country_async"></a>

#### aggregate\_index\_asset\_impact\_scores\_by\_country\_async

```python
async def aggregate_index_asset_impact_scores_by_country_async(
        index_id: str, pathway: str,
        horizon: int) -> StaticListIterator[CountryImpactScore]
```

Get the impact scores for all assets in a market index aggregated by country asynchronously.

<a id="velo_sdk.api.markets.Markets.aggregate_index_asset_climate_scores_by_asset_type"></a>

#### aggregate\_index\_asset\_climate\_scores\_by\_asset\_type

```python
def aggregate_index_asset_climate_scores_by_asset_type(
        index_id: str, pathway: str,
        horizon: int) -> StaticListIterator[AssetTypeClimateScore]
```

Get the climate scores for all assets in a market index aggregated by asset type.

<a id="velo_sdk.api.markets.Markets.aggregate_index_asset_climate_scores_by_asset_type_async"></a>

#### aggregate\_index\_asset\_climate\_scores\_by\_asset\_type\_async

```python
async def aggregate_index_asset_climate_scores_by_asset_type_async(
        index_id: str, pathway: str,
        horizon: int) -> StaticListIterator[AssetTypeClimateScore]
```

Get the climate scores for all assets in a market index aggregated by asset type asynchronously.

<a id="velo_sdk.api.markets.Markets.aggregate_index_asset_impact_scores_by_asset_type"></a>

#### aggregate\_index\_asset\_impact\_scores\_by\_asset\_type

```python
def aggregate_index_asset_impact_scores_by_asset_type(
        index_id: str, pathway: str,
        horizon: int) -> StaticListIterator[AssetTypeImpactScore]
```

Get the impact scores for all assets in a market index aggregated by asset type.

<a id="velo_sdk.api.markets.Markets.aggregate_index_asset_impact_scores_by_asset_type_async"></a>

#### aggregate\_index\_asset\_impact\_scores\_by\_asset\_type\_async

```python
async def aggregate_index_asset_impact_scores_by_asset_type_async(
        index_id: str, pathway: str,
        horizon: int) -> StaticListIterator[AssetTypeImpactScore]
```

Get the impact scores for all assets in a market index aggregated by asset type asynchronously.

<a id="velo_sdk.api.companies"></a>

# velo\_sdk.api.companies

<a id="velo_sdk.api.companies.Companies"></a>

## Companies Objects

```python
class Companies()
```

<a id="velo_sdk.api.companies.Companies.get_company"></a>

#### get\_company

```python
def get_company(company_id: str) -> Company
```

Get a company by its unique ID.

<a id="velo_sdk.api.companies.Companies.get_company_async"></a>

#### get\_company\_async

```python
async def get_company_async(company_id: str) -> Company
```

Get a company by its unique ID asynchronously.

<a id="velo_sdk.api.companies.Companies.list_companies"></a>

#### list\_companies

```python
def list_companies(*,
                   scope: Optional[str] = None,
                   **extra_params: Any) -> PaginatedIterator[Company]
```

List all companies.

<a id="velo_sdk.api.companies.Companies.list_companies_async"></a>

#### list\_companies\_async

```python
async def list_companies_async(
        *,
        scope: Optional[str] = None,
        **extra_params: Any) -> AsyncPaginatedIterator[Company]
```

List all companies asynchronously.

<a id="velo_sdk.api.companies.Companies.search_companies"></a>

#### search\_companies

```python
def search_companies(*,
                     name: Optional[str] = None,
                     **extra_params: Any) -> list[Company]
```

Search for companies by name.

<a id="velo_sdk.api.companies.Companies.search_companies_async"></a>

#### search\_companies\_async

```python
async def search_companies_async(*,
                                 name: Optional[str] = None,
                                 **extra_params: Any) -> list[Company]
```

Search for companies by name asynchronously.

<a id="velo_sdk.api.companies.Companies.list_company_assets"></a>

#### list\_company\_assets

```python
def list_company_assets(company_id: str,
                        **extra_params: Any) -> PaginatedIterator[Asset]
```

List all assets for a company.

<a id="velo_sdk.api.companies.Companies.list_company_assets_async"></a>

#### list\_company\_assets\_async

```python
async def list_company_assets_async(
        company_id: str, **extra_params: Any) -> AsyncPaginatedIterator[Asset]
```

List all assets for a company asynchronously.

<a id="velo_sdk.api.companies.Companies.list_uninsurable_company_assets"></a>

#### list\_uninsurable\_company\_assets

```python
def list_uninsurable_company_assets(
        company_id: str, pathway: str, horizon: int,
        **extra_params: Any) -> PaginatedIterator[AssetClimateScore]
```

List all uninsurable assets for a company.

<a id="velo_sdk.api.companies.Companies.list_uninsurable_company_assets_async"></a>

#### list\_uninsurable\_company\_assets\_async

```python
async def list_uninsurable_company_assets_async(
        company_id: str, pathway: str, horizon: int,
        **extra_params: Any) -> AsyncPaginatedIterator[AssetClimateScore]
```

List all uninsurable assets for a company asynchronously.

<a id="velo_sdk.api.companies.Companies.list_stranded_company_assets"></a>

#### list\_stranded\_company\_assets

```python
def list_stranded_company_assets(
        company_id: str, pathway: str, horizon: int,
        **extra_params: Any) -> PaginatedIterator[AssetClimateScore]
```

List all stranded assets for a company.

<a id="velo_sdk.api.companies.Companies.list_stranded_company_assets_async"></a>

#### list\_stranded\_company\_assets\_async

```python
async def list_stranded_company_assets_async(
        company_id: str, pathway: str, horizon: int,
        **extra_params: Any) -> AsyncPaginatedIterator[AssetClimateScore]
```

List all stranded assets for a company asynchronously.

<a id="velo_sdk.api.companies.Companies.get_company_climate_scores"></a>

#### get\_company\_climate\_scores

```python
def get_company_climate_scores(company_id: str, pathway: str,
                               horizon: int) -> ClimateScore
```

Get the climate scores for a company.

<a id="velo_sdk.api.companies.Companies.get_company_climate_scores_async"></a>

#### get\_company\_climate\_scores\_async

```python
async def get_company_climate_scores_async(company_id: str, pathway: str,
                                           horizon: int) -> ClimateScore
```

Get the climate scores for a company asynchronously.

<a id="velo_sdk.api.companies.Companies.get_company_impact_scores"></a>

#### get\_company\_impact\_scores

```python
def get_company_impact_scores(company_id: str, pathway: str,
                              horizon: int) -> StaticListIterator[ImpactScore]
```

Get the impact scores for a company.

<a id="velo_sdk.api.companies.Companies.get_company_impact_scores_async"></a>

#### get\_company\_impact\_scores\_async

```python
async def get_company_impact_scores_async(
        company_id: str, pathway: str,
        horizon: int) -> StaticListIterator[ImpactScore]
```

Get the impact scores for a company asynchronously.

<a id="velo_sdk.api.companies.Companies.list_company_asset_climate_scores"></a>

#### list\_company\_asset\_climate\_scores

```python
def list_company_asset_climate_scores(
        company_id: str, pathway: str, horizon: int,
        **extra_params: Any) -> PaginatedIterator[AssetClimateScore]
```

Get the climate scores for all assets of a company.

<a id="velo_sdk.api.companies.Companies.list_company_asset_climate_scores_async"></a>

#### list\_company\_asset\_climate\_scores\_async

```python
async def list_company_asset_climate_scores_async(
        company_id: str, pathway: str, horizon: int,
        **extra_params: Any) -> AsyncPaginatedIterator[AssetClimateScore]
```

Get the climate scores for all assets of a company asynchronously.

<a id="velo_sdk.api.companies.Companies.list_company_asset_impact_scores"></a>

#### list\_company\_asset\_impact\_scores

```python
def list_company_asset_impact_scores(
        company_id: str, pathway: str, horizon: int,
        **extra_params: Any) -> PaginatedIterator[AssetImpactScore]
```

Get the impact scores for all assets of a company.

<a id="velo_sdk.api.companies.Companies.list_company_asset_impact_scores_async"></a>

#### list\_company\_asset\_impact\_scores\_async

```python
async def list_company_asset_impact_scores_async(
        company_id: str, pathway: str, horizon: int,
        **extra_params: Any) -> AsyncPaginatedIterator[AssetImpactScore]
```

Get the impact scores for all assets of a company asynchronously.

<a id="velo_sdk.api.companies.Companies.aggregate_company_asset_climate_scores_by_country"></a>

#### aggregate\_company\_asset\_climate\_scores\_by\_country

```python
def aggregate_company_asset_climate_scores_by_country(
        company_id: str, pathway: str,
        horizon: int) -> StaticListIterator[CountryClimateScore]
```

Get the climate scores for all assets of a company aggregated by country.

<a id="velo_sdk.api.companies.Companies.aggregate_company_asset_climate_scores_by_country_async"></a>

#### aggregate\_company\_asset\_climate\_scores\_by\_country\_async

```python
async def aggregate_company_asset_climate_scores_by_country_async(
        company_id: str, pathway: str,
        horizon: int) -> StaticListIterator[CountryClimateScore]
```

Get the climate scores for all assets of a company aggregated by country asynchronously.

<a id="velo_sdk.api.companies.Companies.aggregate_company_asset_impact_scores_by_country"></a>

#### aggregate\_company\_asset\_impact\_scores\_by\_country

```python
def aggregate_company_asset_impact_scores_by_country(
        company_id: str, pathway: str,
        horizon: int) -> StaticListIterator[CountryImpactScore]
```

Get the impact scores for all assets of a company aggregated by country.

<a id="velo_sdk.api.companies.Companies.aggregate_company_asset_impact_scores_by_country_async"></a>

#### aggregate\_company\_asset\_impact\_scores\_by\_country\_async

```python
async def aggregate_company_asset_impact_scores_by_country_async(
        company_id: str, pathway: str,
        horizon: int) -> StaticListIterator[CountryImpactScore]
```

Get the impact scores for all assets of a company aggregated by country asynchronously.

<a id="velo_sdk.api.companies.Companies.aggregate_company_asset_climate_scores_by_asset_type"></a>

#### aggregate\_company\_asset\_climate\_scores\_by\_asset\_type

```python
def aggregate_company_asset_climate_scores_by_asset_type(
        company_id: str, pathway: str,
        horizon: int) -> StaticListIterator[AssetTypeClimateScore]
```

Get the climate scores for all assets of a company aggregated by asset type.

<a id="velo_sdk.api.companies.Companies.aggregate_company_asset_climate_scores_by_asset_type_async"></a>

#### aggregate\_company\_asset\_climate\_scores\_by\_asset\_type\_async

```python
async def aggregate_company_asset_climate_scores_by_asset_type_async(
        company_id: str, pathway: str,
        horizon: int) -> StaticListIterator[AssetTypeClimateScore]
```

Get the climate scores for all assets of a company aggregated by asset type asynchronously.

<a id="velo_sdk.api.companies.Companies.aggregate_company_asset_impact_scores_by_asset_type"></a>

#### aggregate\_company\_asset\_impact\_scores\_by\_asset\_type

```python
def aggregate_company_asset_impact_scores_by_asset_type(
        company_id: str, pathway: str,
        horizon: int) -> StaticListIterator[AssetTypeImpactScore]
```

Get the impact scores for all assets of a company aggregated by asset type.

<a id="velo_sdk.api.companies.Companies.aggregate_company_asset_impact_scores_by_asset_type_async"></a>

#### aggregate\_company\_asset\_impact\_scores\_by\_asset\_type\_async

```python
async def aggregate_company_asset_impact_scores_by_asset_type_async(
        company_id: str, pathway: str,
        horizon: int) -> StaticListIterator[AssetTypeImpactScore]
```

Get the impact scores for all assets of a company aggregated by asset type asynchronously.

<a id="velo_sdk.api.static_list"></a>

# velo\_sdk.api.static\_list

<a id="velo_sdk.api.static_list.StaticListIterator"></a>

## StaticListIterator Objects

```python
class StaticListIterator(Generic[T], Iterator[T], AsyncIterator[T])
```

Helper to fetch, parse, and iterate over a list of items from an API endpoint
that returns the full list under a 'results' key without pagination.

<a id="velo_sdk.api.static_list.StaticListIterator.fetch_all"></a>

#### fetch\_all

```python
def fetch_all() -> List[T]
```

Synchronously fetches all results from the endpoint and parses them.
If data has already been fetched for iteration, returns the cached data.

**Returns**:

  A list of parsed items of type T.

<a id="velo_sdk.api.static_list.StaticListIterator.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__() -> Self
```

Returns the iterator object itself, fetching data if needed.

<a id="velo_sdk.api.static_list.StaticListIterator.__next__"></a>

#### \_\_next\_\_

```python
def __next__() -> T
```

Returns the next item in the fetched list.

<a id="velo_sdk.api.static_list.StaticListIterator.afetch_all"></a>

#### afetch\_all

```python
async def afetch_all() -> List[T]
```

Asynchronously fetches all results from the endpoint and parses them.
If data has already been fetched for iteration, returns the cached data.

**Returns**:

  A list of parsed items of type T.

<a id="velo_sdk.api.static_list.StaticListIterator.__aiter__"></a>

#### \_\_aiter\_\_

```python
def __aiter__() -> Self
```

Returns the async iterator object itself.

<a id="velo_sdk.api.static_list.StaticListIterator.__anext__"></a>

#### \_\_anext\_\_

```python
async def __anext__() -> T
```

Returns the next item, fetching data asynchronously if needed.

<a id="velo_sdk.api.static_list.StaticListIterator.to_polars"></a>

#### to\_polars

```python
def to_polars() -> pl.DataFrame
```

Fetches all results (if not already fetched) and converts them
into a Polars DataFrame.

Assumes that the generic type T is a Pydantic model.

**Returns**:

  A Polars DataFrame containing the fetched data.

<a id="velo_sdk.api.assets"></a>

# velo\_sdk.api.assets

<a id="velo_sdk.api.assets.Assets"></a>

## Assets Objects

```python
class Assets()
```

<a id="velo_sdk.api.assets.Assets.get_asset"></a>

#### get\_asset

```python
def get_asset(asset_id: str) -> Asset
```

Get an asset by its unique ID.

<a id="velo_sdk.api.assets.Assets.get_asset_async"></a>

#### get\_asset\_async

```python
async def get_asset_async(asset_id: str) -> Asset
```

Get an asset by its unique ID asynchronously.

<a id="velo_sdk.api.assets.Assets.list_assets"></a>

#### list\_assets

```python
def list_assets(**extra_params: Any) -> PaginatedIterator[Asset]
```

List all assets.

<a id="velo_sdk.api.assets.Assets.list_assets_async"></a>

#### list\_assets\_async

```python
async def list_assets_async(**extra_params: Any
                            ) -> AsyncPaginatedIterator[Asset]
```

List all assets asynchronously.

<a id="velo_sdk.api.assets.Assets.get_asset_owner"></a>

#### get\_asset\_owner

```python
def get_asset_owner(asset_id: str) -> Company
```

Get the company that owns an asset.

<a id="velo_sdk.api.assets.Assets.get_asset_owner_async"></a>

#### get\_asset\_owner\_async

```python
async def get_asset_owner_async(asset_id: str) -> Company
```

Get the company that owns an asset asynchronously.

<a id="velo_sdk.api.assets.Assets.search_assets"></a>

#### search\_assets

```python
def search_assets(query: str,
                  scope: Literal["public", "company",
                                 "organization"] = "public",
                  company_id: str | None = None,
                  **extra_params: Any) -> PaginatedIterator[Asset]
```

Search for assets.

**Arguments**:

- `query` - The search query string. Asset names and addresses are searched for.
- `scope` - The scope of the search. Can be "public", "company", or "organization".
  "public" is the default scope and searches all available assets in VELO.
  "organization" searches all private assets uploaded to the organization.
  If "company" is selected, `company_id` must also be provided.
- `company_id` - The ID of the company to scope the search to.
  Required if `scope` is "company".
- `**extra_params` - Additional parameters to pass to the API.
  

**Returns**:

  A paginated iterator of assets matching the search criteria.

<a id="velo_sdk.api.assets.Assets.search_assets_async"></a>

#### search\_assets\_async

```python
async def search_assets_async(
        query: str,
        scope: Literal["public", "company", "organization"] = "public",
        company_id: str | None = None,
        **extra_params: Any) -> AsyncPaginatedIterator[Asset]
```

Search for assets asynchronously.

**Arguments**:

- `query` - The search query string. Asset names and addresses are searched for.
- `scope` - The scope of the search. Can be "public", "company", or "organization".
  "public" is the default scope and searches all available assets in VELO.
  "organization" searches all private assets uploaded to the organization.
  If "company" is selected, `company_id` must also be provided.
- `company_id` - The ID of the company to scope the search to.
  Required if `scope` is "company".
- `**extra_params` - Additional parameters to pass to the API.
  

**Returns**:

  A paginated iterator of assets matching the search criteria.

