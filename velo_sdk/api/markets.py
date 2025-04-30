from .base import BaseClient
from .types import (
    CountryClimateScore,
    CountryImpactScore,
    ImpactScore,
    MarketIndex,
    Company,
    ClimateScore,
)
from .pagination import PaginatedIterator, AsyncPaginatedIterator
from .static_list import StaticListIterator


class Markets:
    def __init__(self, client: BaseClient):
        self.client = client

    def list_indexes(self) -> PaginatedIterator[MarketIndex]:
        return PaginatedIterator(
            self.client, "/markets/indexes", {}, item_class=MarketIndex
        )

    async def list_indexes_async(self) -> AsyncPaginatedIterator[MarketIndex]:
        return AsyncPaginatedIterator(
            self.client, "/markets/indexes", {}, item_class=MarketIndex
        )

    def get_index(self, index_id: str) -> MarketIndex:
        response = self.client._request_sync("GET", f"/markets/indexes/{index_id}")
        return MarketIndex(**response)

    async def get_index_async(self, index_id: str) -> MarketIndex:
        response = await self.client._request_async(
            "GET", f"/markets/indexes/{index_id}"
        )
        return MarketIndex(**response)

    def get_index_companies(self, index_id: str) -> PaginatedIterator[Company]:
        return PaginatedIterator(
            self.client,
            f"/markets/indexes/{index_id}/companies",
            {},
            item_class=Company,
        )

    async def get_index_companies_async(
        self, index_id: str
    ) -> AsyncPaginatedIterator[Company]:
        return AsyncPaginatedIterator(
            self.client,
            f"/markets/indexes/{index_id}/companies",
            {},
            item_class=Company,
        )

    def get_index_climate_scores(
        self, index_id: str, pathway: str, horizon: int
    ) -> ClimateScore:
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
        self, index_id: str, pathway: str, horizon: int
    ) -> ClimateScore:
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
        self, index_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[ImpactScore]:
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
        self, index_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[ImpactScore]:
        return StaticListIterator(
            self.client,
            f"/markets/indexes/{index_id}/climate/impacts",
            {
                "pathway": pathway,
                "horizon": horizon,
            },
            item_class=ImpactScore,
        )

    def aggregate_index_asset_climate_scores_by_country(
        self, index_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[CountryClimateScore]:
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
        self, index_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[CountryClimateScore]:
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
        self, index_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[CountryImpactScore]:
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
        self, index_id: str, pathway: str, horizon: int
    ) -> StaticListIterator[CountryImpactScore]:
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
