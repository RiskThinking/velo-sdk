from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterator,
    Optional,
    Type,
    TypeVar,
    AsyncIterator,
)
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class PaginatedIterator(Generic[T], Iterator[T]):
    def __init__(
        self,
        client: Any,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        *,
        item_class: Optional[Type[T]] = None,
        item_parser: Optional[Callable[[Dict[str, Any]], T]] = None,
    ):
        self.client = client
        self.endpoint = endpoint
        self.params = params.copy() if params else {}
        self.buffer: list[T] = []
        self.cursor: Optional[str] = None
        self.finished: bool = False

        # Provide a default parser using Pydantic if not given.
        if item_parser is None:
            if item_class is None:
                raise ValueError(
                    "Either 'item_class' or 'item_parser' must be provided"
                )
            self.item_parser = lambda item: item_class.model_validate(item)
        else:
            self.item_parser = item_parser

    def _fetch_next_page(self) -> None:
        if self.cursor:
            self.params["cursor"] = self.cursor
        response = self.client._request_sync("GET", self.endpoint, params=self.params)
        raw_results = response.get("results", [])
        self.buffer = [self.item_parser(item) for item in raw_results]
        pagination = response.get("pagination", {})
        self.cursor = pagination.get("cursor")
        # Mark finished if it's the last page or no items are returned.
        self.finished = pagination.get("last_page", True) or not self.buffer

    def __iter__(self) -> "PaginatedIterator[T]":
        return self

    def __next__(self) -> T:
        if not self.buffer and not self.finished:
            self._fetch_next_page()
        if self.buffer:
            return self.buffer.pop(0)
        raise StopIteration

    def fetch_page(self) -> list[T]:
        """
        Fetches the next page of results and returns them as a list.
        """
        if not self.buffer and not self.finished:
            self._fetch_next_page()
        page = self.buffer.copy()
        self.buffer.clear()  # Clear the buffer after returning the page.
        return page


class AsyncPaginatedIterator(Generic[T], AsyncIterator[T]):
    def __init__(
        self,
        client: Any,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        *,
        item_class: Optional[Type[T]] = None,
        item_parser: Optional[Callable[[Dict[str, Any]], T]] = None,
    ):
        self.client = client
        self.endpoint = endpoint
        self.params = params.copy() if params else {}
        self.buffer: list[T] = []
        self.cursor: Optional[str] = None
        self.finished: bool = False

        if item_parser is None:
            if item_class is None:
                raise ValueError(
                    "Either 'item_class' or 'item_parser' must be provided"
                )
            self.item_parser = lambda item: item_class.model_validate(item)
        else:
            self.item_parser = item_parser

    async def _fetch_next_page(self) -> None:
        if self.cursor:
            self.params["cursor"] = self.cursor
        response = await self.client._request_async(
            "GET", self.endpoint, params=self.params
        )
        raw_results = response.get("results", [])
        self.buffer = [self.item_parser(item) for item in raw_results]
        pagination = response.get("pagination", {})
        self.cursor = pagination.get("cursor")
        self.finished = pagination.get("last_page", True) or not self.buffer

    def __aiter__(self) -> "AsyncPaginatedIterator[T]":
        return self

    async def __anext__(self) -> T:
        if not self.buffer and not self.finished:
            await self._fetch_next_page()
        if self.buffer:
            return self.buffer.pop(0)
        raise StopAsyncIteration

    async def afetch_page(self) -> list[T]:
        """
        Asynchronously fetches the next page of results and returns them as a list.
        """
        if not self.buffer and not self.finished:
            await self._fetch_next_page()
        page = self.buffer.copy()
        self.buffer.clear()
        return page
