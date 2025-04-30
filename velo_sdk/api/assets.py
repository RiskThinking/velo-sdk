from typing import Any

from .base import BaseClient
from .types import Asset, Company
from .pagination import PaginatedIterator, AsyncPaginatedIterator


class Assets:
    def __init__(self, client: BaseClient):
        self.client = client

    def get_asset(self, asset_id: str) -> Asset:
        response = self.client._request_sync("GET", f"/assets/{asset_id}")
        return Asset(**response)

    async def get_asset_async(self, asset_id: str) -> Asset:
        response = await self.client._request_async("GET", f"/assets/{asset_id}")
        return Asset(**response)

    def list_assets(
        self,
        **extra_params: Any,
    ) -> PaginatedIterator[Asset]:
        return PaginatedIterator(self.client, "/assets", extra_params, item_class=Asset)

    async def list_assets_async(
        self,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[Asset]:
        return AsyncPaginatedIterator(
            self.client, "/assets", extra_params, item_class=Asset
        )

    def get_asset_owner(self, asset_id: str) -> Company:
        response = self.client._request_sync("GET", f"/assets/{asset_id}/ownership")
        return Company(**response)

    async def get_asset_owner_async(self, asset_id: str) -> Company:
        response = await self.client._request_async(
            "GET", f"/assets/{asset_id}/ownership"
        )
        return Company(**response)
