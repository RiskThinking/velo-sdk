from typing import Any, Dict, Literal, Optional
import polars as pl
import io
import csv
import httpx

from velo_sdk.api.errors import APIError

from .base import BaseClient
from .types import (
    AssetClimateScore,
    AssetTypeClimateScore,
    AssetTypeImpactScore,
    Company,
    Sector,
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
        return Company.model_validate(response)

    async def get_company_async(self, company_id: str) -> Company:
        """
        Get a company by its unique ID asynchronously.

        Parameters:
            company_id (str): The unique identifier of the company.

        Returns:
            Company: The Company object.
        """
        response = await self.client._request_async("GET", f"/companies/{company_id}")
        return Company.model_validate(response)

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
            "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact"
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
            "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact"
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
            "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact"
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
            "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact"
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
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
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
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
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
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
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
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=AssetTypeImpactScore,
        )

    def upload_company_assets(
        self, company_id: str, assets: list[Dict] | pl.DataFrame | Any
    ):
        """
        Upload new assets to a company.

        Parameters:
            company_id (str): The unique identifier of the company.
            assets (list[Dict] | pl.DataFrame | pandas.DataFrame): A list of Asset objects to upload,
                   or a DataFrame (pandas or polars) that will be converted to a list of dictionaries.
        """
        required_headers = ["asset_type", "latitude", "longitude", "country"]
        header_mapping = {
            "name": "name",
            "asset_type": "asset_type",
            "city": "city",
            "state": "state",
            "latitude": "latitude",
            "longitude": "longitude",
            "building_footprint": "building_footprint",
            "address": "address",
            "country": "country",
        }

        # Handle pandas DataFrame if available
        try:
            import pandas as pd  # type: ignore

            if isinstance(assets, pd.DataFrame):
                # Map only the columns that exist in both the DataFrame and our expected headers
                for header in required_headers:
                    if header not in assets.columns:  # type: ignore
                        raise ValueError(f"Column {header} is required")

                header_mapping = {
                    header: header_mapping[header]
                    for header in assets.columns  # type: ignore
                    if header in header_mapping
                }
                assets = assets.to_dict("records")  # type: ignore
        except ImportError:
            pass

        # Handle polars DataFrame
        if isinstance(assets, pl.DataFrame):
            # Map only the columns that exist in both the DataFrame and our expected headers
            for header in required_headers:
                if header not in assets.columns:
                    raise ValueError(f"Column {header} is required")

            header_mapping = {
                header: header_mapping[header]
                for header in assets.columns
                if header in header_mapping
            }
            assets = assets.to_dicts()

        # At this point, assets should be a list[Dict] regardless of input type
        if not isinstance(assets, list):
            raise ValueError("Assets must be converted to a list of dictionaries")

        if not assets:
            raise ValueError("Assets list cannot be empty")

        # Create CSV content in memory
        csv_buffer = io.StringIO()

        # Get field names from the first asset record
        fieldnames = list(assets[0].keys())
        writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)

        # Write header and data
        writer.writeheader()
        writer.writerows(assets)

        # Get CSV content as string and convert to bytes
        csv_content = csv_buffer.getvalue()
        csv_buffer.close()

        # Create file-like object for upload
        file_obj = io.BytesIO(csv_content.encode("utf-8"))
        file_obj.seek(0)  # Reset to beginning of file

        # Upload the CSV file using a separate httpx client to avoid header conflicts

        # Create a temporary client just for file upload without default JSON headers
        upload_headers = {
            "Authorization": f"Bearer {self.client._api_key}",
        }

        try:
            with httpx.Client(
                base_url=self.client._base_url, headers=upload_headers
            ) as upload_client:
                response = upload_client.post(
                    f"/companies/{company_id}/assets/upload",
                    files={"file": ("assets.csv", file_obj, "text/csv")},
                )

                # Handle the response the same way as BaseClient
                if response.status_code == 429:
                    from .errors import RateLimitError

                    raise RateLimitError("Rate limit exceeded")
                if response.status_code >= 400:
                    try:
                        error_data = response.json()
                        message = error_data.get(
                            "message", f"HTTP {response.status_code}"
                        )
                        detail = error_data.get("detail")
                        if detail:
                            message = f"{message}: {detail}"
                    except Exception:
                        message = f"HTTP {response.status_code}: {response.text}"
                        error_data = {}

                    raise APIError(
                        message=message,
                        code=error_data.get("code", response.status_code),
                        status=error_data.get(
                            "status", f"{response.status_code} Error"
                        ),
                        timestamp=error_data.get("timestamp"),
                    )

                upload_result = response.json()

        except APIError:
            raise
        except Exception as e:
            raise APIError(f"Failed to upload assets: {e}") from e

        file_id = upload_result["file_id"]

        # Complete the upload with header mapping validation
        completed_upload = self.client._request_sync(
            "PUT",
            f"/companies/{company_id}/assets/upload",
            json={
                "file_id": file_id,
                "header_mapping": header_mapping,
            },
        )

        return completed_upload

    def create_company(self, name: str, sector: Sector) -> Company:
        """
        Create a new company.

        Parameters:
            name (str): The name of the company.
            sector (Sector): The sector of the company.

        Returns:
            Company: The newly created Company object.
        """
        response = self.client._request_sync(
            "POST", "/companies", json={"name": name, "sector": sector}
        )
        return Company.model_validate(response)

    async def create_company_async(self, name: str, sector: Sector) -> Company:
        """
        Create a new company asynchronously.

        Parameters:
            name (str): The name of the company.
            sector (Sector): The GICS sector of the company.

        Returns:
            Company: The newly created Company object.
        """
        response = await self.client._request_async(
            "POST", "/companies", json={"name": name, "sector": sector}
        )
        return Company.model_validate(response)
