from typing import Any, Dict, Optional

from .base import BaseClient
from .types import (
    AssetClimateScore,
    AssetTypeClimateScore,
    AssetTypeImpactScore,
    Company,
    Asset,
    ClimateScore,
    ImpactScore,
    CountryClimateScore,
    CountryImpactScore,
    AssetImpactScore,
)
from .pagination import PaginatedIterator, AsyncPaginatedIterator
from .static_list import StaticListIterator


class Companies:
    def __init__(self, client: BaseClient):
        self.client = client

    def get_company(self, company_id: str) -> Company:
        """
        Get a company by its unique ID.
        """
        response = self.client._request_sync("GET", f"/companies/{company_id}")
        return Company(**response)

    async def get_company_async(self, company_id: str) -> Company:
        """
        Get a company by its unique ID asynchronously.
        """
        response = await self.client._request_async("GET", f"/companies/{company_id}")
        return Company(**response)

    def list_companies(
        self,
        *,
        scope: Optional[str] = None,
        **extra_params: Any,
    ) -> PaginatedIterator[Company]:
        """
        List all companies.
        """
        params: Dict[str, Any] = {}
        if scope is not None:
            params["scope"] = scope
        params.update(extra_params)
        return PaginatedIterator(self.client, "/companies", params, item_class=Company)

    async def list_companies_async(
        self,
        *,
        scope: Optional[str] = None,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[Company]:
        """
        List all companies asynchronously.
        """
        params: Dict[str, Any] = {}
        if scope is not None:
            params["scope"] = scope
        params.update(extra_params)
        return AsyncPaginatedIterator(
            self.client, "/companies", params, item_class=Company
        )

    def search_companies(
        self,
        *,
        name: Optional[str] = None,
        **extra_params: Any,
    ) -> list[Company]:
        """
        Search for companies by name.
        """
        params: Dict[str, Any] = {}
        if name is not None:
            params["name"] = name
        params.update(extra_params)
        response = self.client._request_sync("GET", "/companies/search", params=params)
        results = [Company.model_validate(item) for item in response["results"]]
        return results

    async def search_companies_async(
        self,
        *,
        name: Optional[str] = None,
        **extra_params: Any,
    ) -> list[Company]:
        """
        Search for companies by name asynchronously.
        """
        params: Dict[str, Any] = {}
        if name is not None:
            params["name"] = name
        params.update(extra_params)
        response = await self.client._request_async(
            "GET", "/companies/search", params=params
        )
        results = [Company.model_validate(item) for item in response["results"]]
        return results

    def list_company_assets(
        self,
        company_id: str,
        **extra_params: Any,
    ) -> PaginatedIterator[Asset]:
        """
        List all assets for a company.
        """
        return PaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets",
            extra_params,
            item_class=Asset,
        )

    async def list_company_assets_async(
        self,
        company_id: str,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[Asset]:
        """
        List all assets for a company asynchronously.
        """
        return AsyncPaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets",
            extra_params,
            item_class=Asset,
        )

    def list_uninsurable_company_assets(
        self,
        company_id: str,
        pathway: str,
        horizon: int,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetClimateScore]:
        """
        List all uninsurable assets for a company.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = "var_95"
        params["min_risk"] = 0.35
        params["max_risk"] = 0.75
        params.update(extra_params)
        return PaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores",
            params,
            item_class=AssetClimateScore,
        )

    async def list_uninsurable_company_assets_async(
        self,
        company_id: str,
        pathway: str,
        horizon: int,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetClimateScore]:
        """
        List all uninsurable assets for a company asynchronously.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = "var_95"
        params["min_risk"] = 0.35
        params["max_risk"] = 0.75
        params.update(extra_params)
        return AsyncPaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores",
            params,
            item_class=AssetClimateScore,
        )
    
    def list_stranded_company_assets(
        self,
        company_id: str,
        pathway: str,
        horizon: int,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetClimateScore]:
        """
        List all stranded assets for a company.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = "var_95"
        params["min_risk"] = 0.75
        params.update(extra_params)
        return PaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores",
            params,
            item_class=AssetClimateScore,
        )

    async def list_stranded_company_assets_async(
        self,
        company_id: str,
        pathway: str,
        horizon: int,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetClimateScore]:
        """
        List all stranded assets for a company asynchronously.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = "var_95"
        params["min_risk"] = 0.75
        params.update(extra_params)
        return AsyncPaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores",
            params,
            item_class=AssetClimateScore,
        )

    def get_company_climate_scores(
        self, company_id: str, pathway: str, horizon: int
    ) -> ClimateScore:
        """
        Get the climate scores for a company.
        """
        response = self.client._request_sync(
            "GET",
            f"/companies/{company_id}/climate/scores",
            params={
                "pathway": pathway,
                "horizon": horizon,
            },
        )
        return ClimateScore(**response)

    async def get_company_climate_scores_async(
        self, company_id: str, pathway: str, horizon: int
    ) -> ClimateScore:
        """
        Get the climate scores for a company asynchronously.
        """
        response = await self.client._request_async(
            "GET",
            f"/companies/{company_id}/climate/scores",
            params={
                "pathway": pathway,
                "horizon": horizon,
            },
        )
        return ClimateScore(**response)

    def get_company_impact_scores(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[ImpactScore]:
        """
        Get the impact scores for a company.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/climate/impacts",
            {
                "pathway": pathway,
                "horizon": horizon,
            },
            item_class=ImpactScore,
        )

    async def get_company_impact_scores_async(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[ImpactScore]:
        """
        Get the impact scores for a company asynchronously.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/climate/impacts",
            {
                "pathway": pathway,
                "horizon": horizon,
            },
            item_class=ImpactScore,
        )

    def list_company_asset_climate_scores(
        self,
        company_id: str,
        pathway: str,
        horizon: int,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetClimateScore]:
        """
        Get the climate scores for all assets of a company.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = (
            "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact"
        )
        params.update(extra_params)
        return PaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores",
            params,
            item_class=AssetClimateScore,
        )

    async def list_company_asset_climate_scores_async(
        self,
        company_id: str,
        pathway: str,
        horizon: int,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetClimateScore]:
        """
        Get the climate scores for all assets of a company asynchronously.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = (
            "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact"
        )
        params.update(extra_params)
        return AsyncPaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores",
            params,
            item_class=AssetClimateScore,
        )

    def list_company_asset_impact_scores(
        self,
        company_id: str,
        pathway: str,
        horizon: int,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetImpactScore]:
        """
        Get the impact scores for all assets of a company.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = (
            "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact"
        )
        params.update(extra_params)
        return PaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/impacts",
            params,
            item_class=AssetImpactScore,
        )

    async def list_company_asset_impact_scores_async(
        self,
        company_id: str,
        pathway: str,
        horizon: int,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetImpactScore]:
        """
        Get the impact scores for all assets of a company asynchronously.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = (
            "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact"
        )
        params.update(extra_params)
        return AsyncPaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/impacts",
            params,
            item_class=AssetImpactScore,
        )

    def aggregate_company_asset_climate_scores_by_country(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[CountryClimateScore]:
        """
        Get the climate scores for all assets of a company aggregated by country.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores/aggregation",
            {
                "by": "country",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=CountryClimateScore,
        )

    async def aggregate_company_asset_climate_scores_by_country_async(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[CountryClimateScore]:
        """
        Get the climate scores for all assets of a company aggregated by country asynchronously.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores/aggregation",
            {
                "by": "country",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=CountryClimateScore,
        )

    def aggregate_company_asset_impact_scores_by_country(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[CountryImpactScore]:
        """
        Get the impact scores for all assets of a company aggregated by country.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/impacts/aggregation",
            {
                "by": "country",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=CountryImpactScore,
        )

    async def aggregate_company_asset_impact_scores_by_country_async(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[CountryImpactScore]:
        """
        Get the impact scores for all assets of a company aggregated by country asynchronously.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/impacts/aggregation",
            {
                "by": "country",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=CountryImpactScore,
        )

    def aggregate_company_asset_climate_scores_by_asset_type(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[AssetTypeClimateScore]:
        """
        Get the climate scores for all assets of a company aggregated by asset type.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores/aggregation",
            {
                "by": "asset_type",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=AssetTypeClimateScore,
        )

    async def aggregate_company_asset_climate_scores_by_asset_type_async(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[AssetTypeClimateScore]:
        """
        Get the climate scores for all assets of a company aggregated by asset type asynchronously.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores/aggregation",
            {
                "by": "asset_type",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=AssetTypeClimateScore,
        )

    def aggregate_company_asset_impact_scores_by_asset_type(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[AssetTypeImpactScore]:
        """
        Get the impact scores for all assets of a company aggregated by asset type.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/impacts/aggregation",
            {
                "by": "asset_type",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=AssetTypeImpactScore,
        )

    async def aggregate_company_asset_impact_scores_by_asset_type_async(
        self, company_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[AssetTypeImpactScore]:
        """
        Get the impact scores for all assets of a company aggregated by asset type asynchronously.
        """
        return StaticListIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/impacts/aggregation",
            {
                "by": "asset_type",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=AssetTypeImpactScore,
        )
