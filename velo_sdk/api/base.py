import re
from typing import Any, Dict
import backoff
import httpx
import os
from datetime import datetime
from importlib.metadata import version

from .errors import RateLimitError, APIError, InsufficientCreditsError

BASE_URL = "https://api.riskthinking.ai"

# Matches path prefixes like /v3, /v4, /v10 (version segment at start)
VERSION_PREFIX_PATTERN = re.compile(r"^/v\d+(/|$)")


def _normalize_path(path: str) -> str:
    """
    Normalize the request path for API versioning.
    - Absolute URLs (http:// or https://) are returned as-is (base URL is ignored by httpx).
    - Paths with a version prefix (e.g. /v3/assets, /v4/climate/metrics) are returned as-is.
    - Paths without a version prefix (e.g. /markets/groups) are prefixed with /v3.
    """
    if path.startswith(("http://", "https://")):
        return path
    if VERSION_PREFIX_PATTERN.match(path):
        return path
    return f"/v3{path}" if path.startswith("/") else f"/v3/{path}"


class BaseClient:
    def __init__(
        self,
        api_key: str | None = None,
        timeout: float = 15.0,
        base_url: str | None = None,
    ):
        if api_key is None:
            api_key = os.getenv("RISKTHINKING_API_KEY", None)
        if api_key is None:
            raise Exception("API key is required to initialize the sdk")

        self._api_key = api_key
        self._base_url = (base_url or BASE_URL).rstrip("/")

        sdk_version = version("velo-sdk")

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "User-Agent": f"velo-sdk/{sdk_version}",
        }
        self._sync_client = httpx.Client(
            base_url=self._base_url, headers=headers, timeout=timeout
        )
        self._async_client = httpx.AsyncClient(
            base_url=self._base_url, headers=headers, timeout=timeout
        )

    @backoff.on_exception(backoff.expo, RateLimitError, max_tries=5)
    def _request_sync(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        path = _normalize_path(path)
        response = self._sync_client.request(method, path, **kwargs)
        return self._handle_response_sync(response)

    @backoff.on_exception(backoff.expo, RateLimitError, max_tries=5)
    async def _request_async(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        path = _normalize_path(path)
        response = await self._async_client.request(method, path, **kwargs)
        return await self._handle_response_async(response)

    def _handle_response_sync(self, response: httpx.Response) -> Dict[str, Any]:
        if response.status_code == 429:
            try:
                error = response.json().get("error", {})
            except Exception:
                error = {'timestamp': datetime.now()}
            
            message = str(error.get("message", "Rate limit exceeded"))
            
            # Check if it's a credits error (non-retryable)
            if "Insufficient API credits" in message:
                raise InsufficientCreditsError(
                    message=message,
                    status=error.get("status", f"{response.status_code} Error"),
                    timestamp=error.get("timestamp"),
                )
            
            # Otherwise it's a rate limit (retryable)
            raise RateLimitError(
                message=message,
                status=error.get("status", f"{response.status_code} Error"),
                timestamp=error.get("timestamp"),
            )
        if response.status_code >= 400:
            try:
                error = response.json().get("error", {})
            except Exception:
                error = {'timestamp': datetime.now()}
            raise APIError(
                message=error.get("message", "Unknown error"),
                code=error.get("code", response.status_code),
                status=error.get("status", f"{response.status_code} Error"),
                timestamp=error.get("timestamp"),
            )
        return response.json()

    async def _handle_response_async(self, response: httpx.Response) -> Dict[str, Any]:
        if response.status_code == 429:
            try:
                error = response.json().get("error", {})
            except Exception:
                error = {'timestamp': datetime.now()}
            
            message = str(error.get("message", "Rate limit exceeded"))
            
            # Check if it's a credits error (non-retryable)
            if "Insufficient API credits" in message:
                raise InsufficientCreditsError(
                    message=message,
                    status=error.get("status", f"{response.status_code} Error"),
                    timestamp=error.get("timestamp"),
                )
            
            # Otherwise it's a rate limit (retryable)
            raise RateLimitError(
                message=message,
                status=error.get("status", f"{response.status_code} Error"),
                timestamp=error.get("timestamp"),
            )
        if response.status_code >= 400:
            try:
                json_data = await response.json()
                error = json_data.get("error", {})
            except Exception:
                error = {'timestamp': datetime.now()}
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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.

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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.

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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.
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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.

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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.

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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.

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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.

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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.

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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.

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
        Version prefix /v3 is added only when the endpoint has no version prefix.
        Paths like /v3/assets or /v4/climate/metrics are used as-is.
        Absolute URLs are also supported and used as-is.

        Args:
            path: API endpoint path
            json: JSON body data
            **kwargs: Additional arguments to pass to the request

        Returns:
            API response data as JSON deserialized into a dictionary
        """
        return await self._request_async("PATCH", path, json=json, **kwargs)
