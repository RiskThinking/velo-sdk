from .companies import Companies
from .assets import Assets
from .base import BaseClient
from .markets import Markets
from .climate import Climate


class APIClient(BaseClient):
    def __init__(
        self,
        api_key: str | None = None,
        timeout: float = 15.0,
        base_url: str | None = None,
    ):
        super().__init__(api_key, timeout, base_url)

        # Company endpoints
        self.companies = Companies(self)

        # Asset endpoints
        self.assets = Assets(self)

        # Market endpoints
        self.markets = Markets(self)

        # Climate endpoints
        self.climate = Climate(self)
