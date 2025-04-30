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

        self.api_key = api_key

        self.base_url = BASE_URL if not base_url else base_url
        if not self.base_url.endswith("/v3"):
            self.base_url = self.base_url + "/v3"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        self.sync_client = httpx.Client(
            base_url=self.base_url, headers=headers, timeout=timeout
        )
        self.async_client = httpx.AsyncClient(
            base_url=self.base_url, headers=headers, timeout=timeout
        )

    @backoff.on_exception(backoff.expo, RateLimitError, max_tries=5)
    def _request_sync(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        response = self.sync_client.request(method, path, **kwargs)
        return self._handle_response_sync(response)

    @backoff.on_exception(backoff.expo, RateLimitError, max_tries=5)
    async def _request_async(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        response = await self.async_client.request(method, path, **kwargs)
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
