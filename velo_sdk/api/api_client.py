from .companies import Companies
from .assets import Assets
from .base import BaseClient
from .markets import Markets


class APIClient(BaseClient):
    def __init__(
        self,
        api_key: str | None = None,
        timeout: float = 10.0,
        base_url: str | None = None,
    ):
        super().__init__(api_key, timeout, base_url)

        self.companies = Companies(self)
        self.assets = Assets(self)
        self.markets = Markets(self)
