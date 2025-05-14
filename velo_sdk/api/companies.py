from typing import Any, Dict, Literal, Optional

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
    Pathway,
    HorizonYear,
)
from .pagination import PaginatedIterator, AsyncPaginatedIterator
from .static_list import StaticListIterator


class Companies:
    def __init__(self, client: BaseClient):
        self.client = client

    def get_company(self, company_id: str) -> Company:
        """
        Get a company by its unique ID.

        Parameters:
            company_id (str): The unique identifier of the company.

        Returns:
            Company: The Company object.
        """
        response = self.client._request_sync("GET", f"/companies/{company_id}")
        return Company(**response)

    async def get_company_async(self, company_id: str) -> Company:
        """
        Get a company by its unique ID asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.

        Returns:
            Company: The Company object.
        """
        response = await self.client._request_async("GET", f"/companies/{company_id}")
        return Company(**response)

    def list_companies(
        self,
        *,
        scope: Literal["public", "organization"] = "public",
        **extra_params: Any,
    ) -> PaginatedIterator[Company]:
        """
        List all companies.

        Parameters:
            scope (Literal["public", "organization"]): The scope to filter companies by
                   "public" is the default scope and searches all available companies in VELO.
                   "organization" searches all private companies uploaded to the organization.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            PaginatedIterator[Company]: An iterator over Company objects.
        """
        params: Dict[str, Any] = {}
        params["scope"] = scope
        params.update(extra_params)
        return PaginatedIterator(self.client, "/companies", params, item_class=Company)

    async def list_companies_async(
        self,
        *,
        scope: Literal["public", "organization"] = "public",
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[Company]:
        """
        List all companies asynchronously.

        Parameters:
            scope (Literal["public", "organization"]): The scope to filter companies by
                   "public" is the default scope and searches all available companies in VELO.
                   "organization" searches all private companies uploaded to the organization.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            AsyncPaginatedIterator[Company]: An asynchronous iterator over Company objects.
        """
        params: Dict[str, Any] = {}
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

        Parameters:
            name (Optional[str]): The name of the company to search for.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            list[Company]: A list of Company objects matching the search criteria.
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

        Parameters:
            name (Optional[str]): The name of the company to search for.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            list[Company]: A list of Company objects matching the search criteria.
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

        Parameters:
            company_id (str): The unique identifier of the company.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            PaginatedIterator[Asset]: An iterator over Asset objects belonging to the company.
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

        Parameters:
            company_id (str): The unique identifier of the company.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            AsyncPaginatedIterator[Asset]: An asynchronous iterator over Asset objects belonging to the company.
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
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetClimateScore]:
        """
        List all uninsurable assets for a company.
        Uninsurable assets are defined as those with cvar_95 >= 0.35.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            PaginatedIterator[AssetClimateScore]: An iterator over AssetClimateScore objects for uninsurable assets.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = "cvar_95"
        params["min_risk"] = 0.35
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
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetClimateScore]:
        """
        List all uninsurable assets for a company asynchronously.
        Uninsurable assets are defined as those with cvar_95 >= 0.35.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            AsyncPaginatedIterator[AssetClimateScore]: An asynchronous iterator over AssetClimateScore objects for uninsurable assets.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = "cvar_95"
        params["min_risk"] = 0.35
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
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetClimateScore]:
        """
        List all stranded assets for a company.
        Stranded assets are defined as those with cvar_95 >= 0.75.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            PaginatedIterator[AssetClimateScore]: An iterator over AssetClimateScore objects for stranded assets.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = "cvar_95"
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
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetClimateScore]:
        """
        List all stranded assets for a company asynchronously.
        Stranded assets are defined as those with cvar_95 >= 0.75.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            AsyncPaginatedIterator[AssetClimateScore]: An asynchronous iterator over AssetClimateScore objects for stranded assets.
        """
        params: Dict[str, Any] = {}
        params["pathway"] = pathway
        params["horizon"] = horizon
        params["metric"] = "cvar_95"
        params["min_risk"] = 0.75
        params.update(extra_params)
        return AsyncPaginatedIterator(
            self.client,
            f"/companies/{company_id}/assets/climate/scores",
            params,
            item_class=AssetClimateScore,
        )

    def get_company_climate_scores(
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> ClimateScore:
        """
        Get the climate scores for a company.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            ClimateScore: The ClimateScore object for the company.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> ClimateScore:
        """
        Get the climate scores for a company asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            ClimateScore: The ClimateScore object for the company.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[ImpactScore]:
        """
        Get the impact scores for a company.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[ImpactScore]: An iterator over ImpactScore objects for the company.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[ImpactScore]:
        """
        Get the impact scores for a company asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[ImpactScore]: An asynchronous iterator over ImpactScore objects for the company.
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
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetClimateScore]:
        """
        Get the climate scores for all assets of a company.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            PaginatedIterator[AssetClimateScore]: An iterator over AssetClimateScore objects for the company's assets.
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
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetClimateScore]:
        """
        Get the climate scores for all assets of a company asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            AsyncPaginatedIterator[AssetClimateScore]: An asynchronous iterator over AssetClimateScore objects for the company's assets.
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
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetImpactScore]:
        """
        Get the impact scores for all assets of a company.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            PaginatedIterator[AssetImpactScore]: An iterator over AssetImpactScore objects for the company's assets.
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
            df_transform=lambda asset: [
                {
                    "asset_id": asset.asset_id,
                    **{
                        f"index_{risk.index_name}": risk.index_impact_cvar_50
                        for risk in asset.index_risks
                    },
                }
            ],
        )

    async def list_company_asset_impact_scores_async(
        self,
        company_id: str,
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetImpactScore]:
        """
        Get the impact scores for all assets of a company asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            AsyncPaginatedIterator[AssetImpactScore]: An asynchronous iterator over AssetImpactScore objects for the company's assets.
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
            df_transform=lambda asset: [
                {
                    "asset_id": asset.asset_id,
                    **{
                        f"index_{risk.index_name}": risk.index_impact_cvar_50
                        for risk in asset.index_risks
                    },
                }
            ],
        )

    def aggregate_company_asset_climate_scores_by_country(
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[CountryClimateScore]:
        """
        Get the climate scores for all assets of a company aggregated by country.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[CountryClimateScore]: An iterator over CountryClimateScore objects, aggregated by country.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[CountryClimateScore]:
        """
        Get the climate scores for all assets of a company aggregated by country asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[CountryClimateScore]: An asynchronous iterator over CountryClimateScore objects, aggregated by country.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[CountryImpactScore]:
        """
        Get the impact scores for all assets of a company aggregated by country.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[CountryImpactScore]: An iterator over CountryImpactScore objects, aggregated by country.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[CountryImpactScore]:
        """
        Get the impact scores for all assets of a company aggregated by country asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[CountryImpactScore]: An asynchronous iterator over CountryImpactScore objects, aggregated by country.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[AssetTypeClimateScore]:
        """
        Get the climate scores for all assets of a company aggregated by asset type.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[AssetTypeClimateScore]: An iterator over AssetTypeClimateScore objects, aggregated by asset type.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[AssetTypeClimateScore]:
        """
        Get the climate scores for all assets of a company aggregated by asset type asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[AssetTypeClimateScore]: An asynchronous iterator over AssetTypeClimateScore objects, aggregated by asset type.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[AssetTypeImpactScore]:
        """
        Get the impact scores for all assets of a company aggregated by asset type.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[AssetTypeImpactScore]: An iterator over AssetTypeImpactScore objects, aggregated by asset type.
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
        self, company_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[AssetTypeImpactScore]:
        """
        Get the impact scores for all assets of a company aggregated by asset type asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[AssetTypeImpactScore]: An asynchronous iterator over AssetTypeImpactScore objects, aggregated by asset type.
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
