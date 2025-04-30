from pydantic import BaseModel


class Company(BaseModel):
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
    id: str
    name: str
    sectors: list[str]
    created_at: str
    updated_at: str
    organization_id: str | None = None


class ClimateScore(BaseModel):
    dcr_score: float | None = None
    expected_impact: float | None = None
    cvar_99: float | None = None
    cvar_95: float | None = None
    cvar_50: float | None = None
    var_99: float | None = None
    var_95: float | None = None
    var_50: float | None = None


class ImpactScore(BaseModel):
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
    asset_count: int
    country: str


class CountryImpactScore(ImpactScore):
    asset_count: int
    country: str

class AssetClimateScore(ClimateScore):
    asset_id: str
    asset_type: str
    country: str
    state: str
    city: str
    address: str

class AssetImpactScore(BaseModel):
    asset_id: str
    index_risks: list[ImpactScore]