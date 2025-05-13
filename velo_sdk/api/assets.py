from typing import Any, Literal

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

    def search_assets(
        self,
        query: str,
        scope: Literal["public", "company", "organization"] = "public",
        company_id: str | None = None,
        **extra_params: Any,
    ) -> PaginatedIterator[Asset]:
        """
        Search for assets.

        Parameters:
            query: The search query string. Asset names and addresses are searched for.
            scope: The scope of the search. Can be "public", "company", or "organization".
                   "public" is the default scope and searches all available assets in VELO.
                   "organization" searches all private assets uploaded to the organization.
                   If "company" is selected, `company_id` must also be provided.
            company_id: The ID of the company to scope the search to.
                        Required if `scope` is "company".
            **extra_params: Additional parameters to pass to the API.

        Returns:
            A paginated iterator of assets matching the search criteria.
        """
        params = {
            "query": query,
            "scope": scope,
            "company_id": company_id,
            **extra_params,
        }
        params = {k: v for k, v in params.items() if v is not None}
        return PaginatedIterator(
            self.client, "/assets/search", params, item_class=Asset
        )

    async def search_assets_async(
        self,
        query: str,
        scope: Literal["public", "company", "organization"] = "public",
        company_id: str | None = None,
        **extra_params: Any,
    ) -> AsyncPaginatedIterator[Asset]:
        """
        Search for assets asynchronously.

        Parameters:
            query: The search query string. Asset names and addresses are searched for.
            scope: The scope of the search. Can be "public", "company", or "organization".
                   "public" is the default scope and searches all available assets in VELO.
                   "organization" searches all private assets uploaded to the organization.
                   If "company" is selected, `company_id` must also be provided.
            company_id: The ID of the company to scope the search to.
                        Required if `scope` is "company".
            **extra_params: Additional parameters to pass to the API.

        Returns:
            A paginated iterator of assets matching the search criteria.
        """
        params = {
            "query": query,
            "scope": scope,
            "company_id": company_id,
            **extra_params,
        }
        params = {k: v for k, v in params.items() if v is not None}
        return AsyncPaginatedIterator(
            self.client, "/assets/search", params, item_class=Asset
        )
