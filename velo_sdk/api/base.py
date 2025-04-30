from typing import Any, Dict
import backoff
import httpx
import os

from .errors import RateLimitError, APIError

BASE_URL = "https://api.riskthinking.ai/v3"


class BaseClient:
    def __init__(
        self,
        api_key: str | None = None,
        timeout: float = 10.0,
        base_url: str | None = None,
    ):
        if api_key is None:
            api_key = os.getenv("RISKTHINKING_API_KEY", None)
        if api_key is None:
            raise Exception("API key is required to initialize the sdk")

        self._api_key = api_key

        self._base_url = BASE_URL if not base_url else base_url
        if not self._base_url.endswith("/v3"):
            self._base_url = self._base_url + "/v3"

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        self._sync_client = httpx.Client(
            base_url=self._base_url, headers=headers, timeout=timeout
        )
        self._async_client = httpx.AsyncClient(
            base_url=self._base_url, headers=headers, timeout=timeout
        )

    @backoff.on_exception(backoff.expo, RateLimitError, max_tries=5)
    def _request_sync(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        # Remove the /v3 prefix since it's part of the base URL
        if path.startswith("/v3"):
            path = path[3:]
        response = self._sync_client.request(method, path, **kwargs)
        return self._handle_response_sync(response)

    @backoff.on_exception(backoff.expo, RateLimitError, max_tries=5)
    async def _request_async(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        # Remove the /v3 prefix since it's part of the base URL
        if path.startswith("/v3"):
            path = path[3:]
        response = await self._async_client.request(method, path, **kwargs)
        return await self._handle_response_async(response)

    def _handle_response_sync(self, response: httpx.Response) -> Dict[str, Any]:
        if response.status_code == 429:
            raise RateLimitError("Rate limit exceeded")
        if response.status_code >= 400:
            try:
                error = response.json().get("error", {})
            except Exception:
                error = {}
            raise APIError(
                message=error.get("message", "Unknown error"),
                code=error.get("code", response.status_code),
                status=error.get("status", f"{response.status_code} Error"),
                timestamp=error.get("timestamp"),
            )
        return response.json()

    async def _handle_response_async(self, response: httpx.Response) -> Dict[str, Any]:
        if response.status_code == 429:
            raise RateLimitError("Rate limit exceeded")
        if response.status_code >= 400:
            try:
                json_data = await response.json()
                error = json_data.get("error", {})
            except Exception:
                error = {}
            raise APIError(
                message=error.get("message", "Unknown error"),
                code=error.get("code", response.status_code),
                status=error.get("status", f"{response.status_code} Error"),
                timestamp=error.get("timestamp"),
            )
        return await response.json()

    # Generic HTTP methods
    def get(
        self, path: str, params: Dict[str, Any] = dict(), **kwargs
    ) -> Dict[str, Any]:
        """
        Make a GET request to the API.
        The version /v3 is automatically added to the path.

        Args:
            path: API endpoint path
            params: Query parameters
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return self._request_sync("GET", path, params=params, **kwargs)

    async def get_async(
        self, path: str, params: Dict[str, Any] = dict(), **kwargs
    ) -> Dict[str, Any]:
        """
        Make an asynchronous GET request to the API.
        The version /v3 is automatically added to the path.

        Args:
            path: API endpoint path
            params: Query parameters
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return await self._request_async("GET", path, params=params, **kwargs)

    def post(
        self, path: str, json: Dict[str, Any] = dict(), **kwargs
    ) -> Dict[str, Any]:
        """
        Make a POST request to the API.
        The version /v3 is automatically added to the path.
        Args:
            path: API endpoint path
            json: JSON body data
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return self._request_sync("POST", path, json=json, **kwargs)

    async def post_async(
        self, path: str, json: Dict[str, Any] = dict(), **kwargs
    ) -> Dict[str, Any]:
        """
        Make an asynchronous POST request to the API.
        The version /v3 is automatically added to the path.

        Args:
            path: API endpoint path
            json: JSON body data
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return await self._request_async("POST", path, json=json, **kwargs)

    def put(self, path: str, json: Dict[str, Any] = dict(), **kwargs) -> Dict[str, Any]:
        """
        Make a PUT request to the API.
        The version /v3 is automatically added to the path.

        Args:
            path: API endpoint path
            json: JSON body data
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return self._request_sync("PUT", path, json=json, **kwargs)

    async def put_async(
        self, path: str, json: Dict[str, Any] = dict(), **kwargs
    ) -> Dict[str, Any]:
        """
        Make an asynchronous PUT request to the API.
        The version /v3 is automatically added to the path.

        Args:
            path: API endpoint path
            json: JSON body data
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return await self._request_async("PUT", path, json=json, **kwargs)

    def delete(self, path: str, **kwargs) -> Dict[str, Any]:
        """
        Make a DELETE request to the API.
        The version /v3 is automatically added to the path.

        Args:
            path: API endpoint path
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return self._request_sync("DELETE", path, **kwargs)

    async def delete_async(self, path: str, **kwargs) -> Dict[str, Any]:
        """
        Make an asynchronous DELETE request to the API.
        The version /v3 is automatically added to the path.

        Args:
            path: API endpoint path
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return await self._request_async("DELETE", path, **kwargs)

    def patch(
        self, path: str, json: Dict[str, Any] = dict(), **kwargs
    ) -> Dict[str, Any]:
        """
        Make a PATCH request to the API.
        The version /v3 is automatically added to the path.

        Args:
            path: API endpoint path
            json: JSON body data
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return self._request_sync("PATCH", path, json=json, **kwargs)

    async def patch_async(
        self, path: str, json: Dict[str, Any] = dict(), **kwargs
    ) -> Dict[str, Any]:
        """
        Make an asynchronous PATCH request to the API.
        The version /v3 is automatically added to the path.

        Args:
            path: API endpoint path
            json: JSON body data
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return await self._request_async("PATCH", path, json=json, **kwargs)
