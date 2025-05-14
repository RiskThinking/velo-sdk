from typing import Any, Dict, Optional
from .base import BaseClient
from .types import (
    AssetClimateScore,
    AssetImpactScore,
    AssetTypeClimateScore,
    AssetTypeImpactScore,
    CountryClimateScore,
    CountryImpactScore,
    ImpactScore,
    MarketIndex,
    Company,
    ClimateScore,
    Pathway,
    HorizonYear,
)
from .pagination import PaginatedIterator, AsyncPaginatedIterator
from .static_list import StaticListIterator


class Markets:
    def __init__(self, client: BaseClient):
        self.client = client

    def search_indexes(
        self,
        *,
        name: Optional[str] = None,
        **extra_params: Any,
    ) -> list[MarketIndex]:
        """
        Search for market indexes by name.

        Parameters:
            name (Optional[str]): The name of the market index to search for.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            list[MarketIndex]: A list of MarketIndex objects matching the search criteria.
        """
        params: Dict[str, Any] = {}
        if name is not None:
            params["name"] = name
        params.update(extra_params)
        response = self.client._request_sync(
            "GET", "/markets/indexes/search", params=params
        )
        results = [MarketIndex.model_validate(item) for item in response["results"]]
        return results

    async def search_indexes_async(
        self,
        *,
        name: Optional[str] = None,
        **extra_params: Any,
    ) -> list[MarketIndex]:
        """
        Search for market indexes by name asynchronously.

        Parameters:
            name (Optional[str]): The name of the market index to search for.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            list[MarketIndex]: A list of MarketIndex objects matching the search criteria.
        """
        params: Dict[str, Any] = {}
        if name is not None:
            params["name"] = name
        params.update(extra_params)
        response = await self.client._request_async(
            "GET", "/markets/indexes/search", params=params
        )
        results = [MarketIndex.model_validate(item) for item in response["results"]]
        return results

    def list_indexes(self) -> PaginatedIterator[MarketIndex]:
        """
        List all market indexes.

        Returns:
            PaginatedIterator[MarketIndex]: An iterator over MarketIndex objects.
        """
        return PaginatedIterator(
            self.client, "/markets/indexes", {}, item_class=MarketIndex
        )

    async def list_indexes_async(self) -> AsyncPaginatedIterator[MarketIndex]:
        """
        List all market indexes asynchronously.

        Returns:
            AsyncPaginatedIterator[MarketIndex]: An asynchronous iterator over MarketIndex objects.
        """
        return AsyncPaginatedIterator(
            self.client, "/markets/indexes", {}, item_class=MarketIndex
        )

    def get_index(self, index_id: str) -> MarketIndex:
        """
        Get a market index by its unique ID.

        Parameters:
            index_id (str): The unique identifier of the market index.

        Returns:
            MarketIndex: The MarketIndex object.
        """
        response = self.client._request_sync("GET", f"/markets/indexes/{index_id}")
        return MarketIndex(**response)

    async def get_index_async(self, index_id: str) -> MarketIndex:
        """
        Get a market index by its unique ID asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.

        Returns:
            MarketIndex: The MarketIndex object.
        """
        response = await self.client._request_async(
            "GET", f"/markets/indexes/{index_id}"
        )
        return MarketIndex(**response)

    def get_index_companies(self, index_id: str) -> PaginatedIterator[Company]:
        """
        Get all companies in a market index.

        Parameters:
            index_id (str): The unique identifier of the market index.

        Returns:
            PaginatedIterator[Company]: An iterator over Company objects in the index.
        """
        return PaginatedIterator(
            self.client,
            f"/markets/indexes/{index_id}/companies",
            {},
            item_class=Company,
        )

    async def get_index_companies_async(
        self, index_id: str
    ) -> AsyncPaginatedIterator[Company]:
        """
        Get all companies in a market index asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.

        Returns:
            AsyncPaginatedIterator[Company]: An asynchronous iterator over Company objects in the index.
        """
        return AsyncPaginatedIterator(
            self.client,
            f"/markets/indexes/{index_id}/companies",
            {},
            item_class=Company,
        )

    def get_index_climate_scores(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> ClimateScore:
        """
        Get the climate scores for a market index.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            ClimateScore: The ClimateScore object for the market index.
        """
        response = self.client._request_sync(
            "GET",
            f"/markets/indexes/{index_id}/climate/scores",
            params={
                "pathway": pathway,
                "horizon": horizon,
            },
        )
        return ClimateScore(**response)

    async def get_index_climate_scores_async(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> ClimateScore:
        """
        Get the climate scores for a market index asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            ClimateScore: The ClimateScore object for the market index.
        """
        response = await self.client._request_async(
            "GET",
            f"/markets/indexes/{index_id}/climate/scores",
            params={
                "pathway": pathway,
                "horizon": horizon,
            },
        )
        return ClimateScore(**response)

    def get_index_impact_scores(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[ImpactScore]:
        """
        Get the impact scores for a market index.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[ImpactScore]: An iterator over ImpactScore objects for the market index.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/climate/impacts",
            {
                "pathway": pathway,
                "horizon": horizon,
            },
            item_class=ImpactScore,
        )

    async def get_index_impact_scores_async(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[ImpactScore]:
        """
        Get the impact scores for a market index asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[ImpactScore]: An asynchronous iterator over ImpactScore objects for the market index.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/climate/impacts",
            {
                "pathway": pathway,
                "horizon": horizon,
            },
            item_class=ImpactScore,
        )

    def list_index_asset_impact_scores(
        self,
        index_id: str,
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetImpactScore]:
        """
        Get the impact scores for all assets of a market index.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            PaginatedIterator[AssetImpactScore]: An iterator over AssetImpactScore objects for the index's assets.
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
            f"/markets/indexes/{index_id}/assets/climate/impacts",
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

    def list_index_asset_climate_scores(
        self,
        index_id: str,
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> PaginatedIterator[AssetClimateScore]:
        """
        Get the climate scores for all assets of a market index.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            PaginatedIterator[AssetClimateScore]: An iterator over AssetClimateScore objects for the index's assets.
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
            f"/markets/indexes/{index_id}/assets/climate/scores",
            params,
            item_class=AssetClimateScore,
        )

    async def list_index_asset_climate_scores_async(
        self,
        index_id: str,
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetClimateScore]:
        """
        Get the climate scores for all assets of a market index asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            AsyncPaginatedIterator[AssetClimateScore]: An asynchronous iterator over AssetClimateScore objects for the index's assets.
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
            f"/markets/indexes/{index_id}/assets/climate/scores",
            params,
            item_class=AssetClimateScore,
        )

    async def list_index_asset_impact_scores_async(
        self,
        index_id: str,
        pathway: Pathway,
        horizon: HorizonYear,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[AssetImpactScore]:
        """
        Get the impact scores for all assets of a market index asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.
            **extra_params (Any): Additional parameters to pass to the API.

        Returns:
            AsyncPaginatedIterator[AssetImpactScore]: An asynchronous iterator over AssetImpactScore objects for the index's assets.
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
            f"/markets/indexes/{index_id}/assets/climate/impacts",
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

    def aggregate_index_asset_climate_scores_by_country(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[CountryClimateScore]:
        """
        Get the climate scores for all assets in a market index aggregated by country.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[CountryClimateScore]: An iterator over CountryClimateScore objects, aggregated by country.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/assets/climate/scores/aggregation",
            {
                "by": "country",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=CountryClimateScore,
        )

    async def aggregate_index_asset_climate_scores_by_country_async(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[CountryClimateScore]:
        """
        Get the climate scores for all assets in a market index aggregated by country asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[CountryClimateScore]: An asynchronous iterator over CountryClimateScore objects, aggregated by country.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/assets/climate/scores/aggregation",
            {
                "by": "country",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=CountryClimateScore,
        )

    def aggregate_index_asset_impact_scores_by_country(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[CountryImpactScore]:
        """
        Get the impact scores for all assets in a market index aggregated by country.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[CountryImpactScore]: An iterator over CountryImpactScore objects, aggregated by country.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/assets/climate/impacts/aggregation",
            {
                "by": "country",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=CountryImpactScore,
        )

    async def aggregate_index_asset_impact_scores_by_country_async(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[CountryImpactScore]:
        """
        Get the impact scores for all assets in a market index aggregated by country asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[CountryImpactScore]: An asynchronous iterator over CountryImpactScore objects, aggregated by country.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/assets/climate/impacts/aggregation",
            {
                "by": "country",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=CountryImpactScore,
        )

    def aggregate_index_asset_climate_scores_by_asset_type(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[AssetTypeClimateScore]:
        """
        Get the climate scores for all assets in a market index aggregated by asset type.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[AssetTypeClimateScore]: An iterator over AssetTypeClimateScore objects, aggregated by asset type.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/assets/climate/scores/aggregation",
            {
                "by": "asset_type",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=AssetTypeClimateScore,
        )

    async def aggregate_index_asset_climate_scores_by_asset_type_async(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[AssetTypeClimateScore]:
        """
        Get the climate scores for all assets in a market index aggregated by asset type asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[AssetTypeClimateScore]: An asynchronous iterator over AssetTypeClimateScore objects, aggregated by asset type.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/assets/climate/scores/aggregation",
            {
                "by": "asset_type",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "dcr_score,cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=AssetTypeClimateScore,
        )

    def aggregate_index_asset_impact_scores_by_asset_type(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[AssetTypeImpactScore]:
        """
        Get the impact scores for all assets in a market index aggregated by asset type.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[AssetTypeImpactScore]: An iterator over AssetTypeImpactScore objects, aggregated by asset type.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/assets/climate/impacts/aggregation",
            {
                "by": "asset_type",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=AssetTypeImpactScore,
        )

    async def aggregate_index_asset_impact_scores_by_asset_type_async(
        self, index_id: str, pathway: Pathway, horizon: HorizonYear
    ) -> StaticListIterator[AssetTypeImpactScore]:
        """
        Get the impact scores for all assets in a market index aggregated by asset type asynchronously.

        Parameters:
            index_id (str): The unique identifier of the market index.
            pathway (Pathway): Climate scenario pathway powered by Climate Earth Digital Twin.
            horizon (HorizonYear): Climatology year representing a decadal period.

        Returns:
            StaticListIterator[AssetTypeImpactScore]: An asynchronous iterator over AssetTypeImpactScore objects, aggregated by asset type.
        """
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/assets/climate/impacts/aggregation",
            {
                "by": "asset_type",
                "pathway": pathway,
                "horizon": horizon,
                "metric": "cvar_99,var_99,cvar_95,var_95,cvar_50,var_50,expected_impact",
            },
            item_class=AssetTypeImpactScore,
        )
