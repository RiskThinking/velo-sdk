from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    Type,
    TypeVar,
    Iterator,
    AsyncIterator,
    Self,
)
from pydantic import BaseModel
import polars as pl

T = TypeVar("T", bound=BaseModel)


class StaticListIterator(Generic[T], Iterator[T], AsyncIterator[T]):
    """
    Helper to fetch, parse, and iterate over a list of items from an API endpoint
    that returns the full list under a 'results' key without pagination.
    """

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

        if item_parser is None:
            if item_class is None:
                raise ValueError(
                    "Either 'item_class' or 'item_parser' must be provided"
                )
            self.item_parser: Callable[[Dict[str, Any]], T] = (
                lambda item: item_class.model_validate(item)
            )
        else:
            self.item_parser = item_parser

        # Internal state for iteration
        self._fetched_data: Optional[List[T]] = None
        self._iter_index: int = 0

    def _fetch_sync_if_needed(self) -> None:
        """Fetches data synchronously if not already fetched."""
        if self._fetched_data is None:
            self._fetched_data = self.fetch_all()  # Use the existing fetch method
            self._iter_index = 0  # Reset index when fetching

    def fetch_all(self) -> List[T]:
        """
        Synchronously fetches all results from the endpoint and parses them.
        If data has already been fetched for iteration, returns the cached data.

        Returns:
            A list of parsed items of type T.
        """
        if self._fetched_data is None:
            # Fetch and store internally
            response = self.client._request_sync(
                "GET", self.endpoint, params=self.params
            )
            raw_results = response.get("results", [])
            if not isinstance(raw_results, list):
                raise TypeError(
                    f"Expected 'results' field to be a list, got {type(raw_results)}"
                )
            self._fetched_data = [self.item_parser(item) for item in raw_results]
            self._iter_index = 0  # Ensure index is reset

        # Return a copy to prevent external modification of internal state
        return self._fetched_data.copy()

    def __iter__(self) -> Self:
        """Returns the iterator object itself, fetching data if needed."""
        self._fetch_sync_if_needed()
        return self

    def __next__(self) -> T:
        """Returns the next item in the fetched list."""
        self._fetch_sync_if_needed()  # Ensure data is fetched
        if self._fetched_data is not None and self._iter_index < len(
            self._fetched_data
        ):
            item = self._fetched_data[self._iter_index]
            self._iter_index += 1
            return item
        else:
            raise StopIteration

    async def _afetch_async_if_needed(self) -> None:
        """Fetches data asynchronously if not already fetched."""
        if self._fetched_data is None:
            self._fetched_data = (
                await self.afetch_all()
            )  # Use the existing async fetch method
            self._iter_index = 0  # Reset index

    async def afetch_all(self) -> List[T]:
        """
        Asynchronously fetches all results from the endpoint and parses them.
        If data has already been fetched for iteration, returns the cached data.

        Returns:
            A list of parsed items of type T.
        """
        if self._fetched_data is None:
            # Fetch and store internally
            response = await self.client._request_async(
                "GET", self.endpoint, params=self.params
            )
            raw_results = response.get("results", [])
            if not isinstance(raw_results, list):
                raise TypeError(
                    f"Expected 'results' field to be a list, got {type(raw_results)}"
                )
            self._fetched_data = [self.item_parser(item) for item in raw_results]
            self._iter_index = 0  # Ensure index is reset

        # Return a copy
        return self._fetched_data.copy()

    def __aiter__(self) -> Self:
        """Returns the async iterator object itself."""
        return self

    async def __anext__(self) -> T:
        """Returns the next item, fetching data asynchronously if needed."""
        await self._afetch_async_if_needed()  # Ensure data is fetched
        if self._fetched_data is not None and self._iter_index < len(
            self._fetched_data
        ):
            item = self._fetched_data[self._iter_index]
            self._iter_index += 1
            return item
        else:
            raise StopAsyncIteration

    def to_polars(self) -> pl.DataFrame:
        """
        Fetches all results (if not already fetched) and converts them
        into a Polars DataFrame.

        Assumes that the generic type T is a Pydantic model.

        Returns:
            A Polars DataFrame containing the fetched data.
        """
        self._fetch_sync_if_needed()  # Ensure data is available

        if self._fetched_data is None or not self._fetched_data:
            return pl.DataFrame()  # Return empty DataFrame if no data

        # Convert list of Pydantic models to list of dictionaries
        data_dicts = [item.model_dump() for item in self._fetched_data]

        # Create Polars DataFrame from the list of dictionaries
        df = pl.from_dicts(data_dicts)
        return df
