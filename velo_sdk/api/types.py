from pydantic import BaseModel


class Company(BaseModel):
    """
    A company is an entity that has assets and identifying information.
    """
    id: str
    name: str
    slug: str
    headquarters_address: str
    organization_id: str | None = None
    market_cap: int
    annual_revenue: int
    headquarters_country: str
    sector: str
    isin_codes: list[str]
    figi_codes: list[str]
    cik_code: str
    lei_code: str
    stock_tickers: list[str]
    is_grandparent: bool | None = None
    data_generated_at: str | None = None
    data_generation_status: str | None = None
    created_at: str
    updated_at: str


class Asset(BaseModel):
    """
    An asset represents aphysical asset that is subject to climate risk.
    """
    id: str
    name: str
    asset_type: str
    asset_function: str
    asset_category: str
    city: str
    state: str
    latitude: float
    longitude: float
    building_footprint: float
    asset_value: int
    address: str
    hex_id: int
    country: str
    ipcc_region: str
    materiality_score: float
    created_at: str
    updated_at: str


class MarketIndex(BaseModel):
    """
    A market index is a collection of companies.
    """
    id: str
    name: str
    sectors: list[str]
    created_at: str
    updated_at: str
    organization_id: str | None = None


class ClimateScore(BaseModel):
    """
    The cimate risk metrics that represent the likelihood of a company or asset to be impacted by climate risk.
    """
    dcr_score: float | None = None
    expected_impact: float | None = None
    cvar_99: float | None = None
    cvar_95: float | None = None
    cvar_50: float | None = None
    var_99: float | None = None
    var_95: float | None = None
    var_50: float | None = None


class ImpactScore(BaseModel):
    """
    The impact risk metrics that represent the potential impact of a company or asset to be impacted by climate risk.
    These metrics represent an individual risk factor and its attribution to the total climate risk metrics.
    """
    index_name: str
    index_impact_cvar_50: float | None = None
    index_impact_cvar_95: float | None = None
    index_impact_cvar_99: float | None = None
    index_impact_var_50: float | None = None
    index_impact_var_95: float | None = None
    index_impact_var_99: float | None = None
    index_impact_expected: float | None = None
    index_attribution_expected: float | None = None
    index_attribution_var_99: float | None = None
    index_attribution_var_95: float | None = None
    index_attribution_var_50: float | None = None
    index_attribution_cvar_99: float | None = None
    index_attribution_cvar_95: float | None = None
    index_attribution_cvar_50: float | None = None


class CountryClimateScore(ClimateScore):
    """
    Climate risk metrics aggregated for a country.
    """
    asset_count: int
    country: str


class CountryImpactScore(ImpactScore):
    """
    Impact risk metrics aggregated for a country.
    """
    asset_count: int
    country: str

class AssetTypeClimateScore(ClimateScore):
    """
    Climate risk metrics aggregated for an asset type.
    """
    asset_count: int
    asset_type: str


class AssetTypeImpactScore(ImpactScore):
    """
    Impact risk metrics aggregated for an asset type.
    """
    asset_count: int
    asset_type: str

class AssetClimateScore(ClimateScore):
    """
    Climate risk metrics for an asset.
    """
    asset_id: str
    asset_type: str
    country: str
    state: str
    city: str
    address: str

class AssetImpactScore(BaseModel):
    """
    Impact risk metrics for an asset.
    """
    asset_id: str
    index_risks: list[ImpactScore]