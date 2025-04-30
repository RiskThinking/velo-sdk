from typing import Any

from .base import BaseClient
from .types import Asset, Company
from .pagination import PaginatedIterator, AsyncPaginatedIterator


class Assets:
    def __init__(self, client: BaseClient):
        self.client = client

    def get_asset(self, asset_id: str) -> Asset:
        """
        Get an asset by its unique ID.
        """
        response = self.client._request_sync("GET", f"/assets/{asset_id}")
        return Asset(**response)

    async def get_asset_async(self, asset_id: str) -> Asset:
        """
        Get an asset by its unique ID asynchronously.
        """
        response = await self.client._request_async("GET", f"/assets/{asset_id}")
        return Asset(**response)

    def list_assets(
        self,
        **extra_params: Any,
    ) -> PaginatedIterator[Asset]:
        """
        List all assets.
        """
        return PaginatedIterator(self.client, "/assets", extra_params, item_class=Asset)

    async def list_assets_async(
        self,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[Asset]:
        """
        List all assets asynchronously.
        """
        return AsyncPaginatedIterator(
            self.client, "/assets", extra_params, item_class=Asset
        )

    def get_asset_owner(self, asset_id: str) -> Company:
        """
        Get the company that owns an asset.
        """
        response = self.client._request_sync("GET", f"/assets/{asset_id}/ownership")
        return Company(**response)

    async def get_asset_owner_async(self, asset_id: str) -> Company:
        """
        Get the company that owns an asset asynchronously.
        """
        response = await self.client._request_async(
            "GET", f"/assets/{asset_id}/ownership"
        )
        return Company(**response)
