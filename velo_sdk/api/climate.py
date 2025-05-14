from .base import BaseClient


class Climate:
    def __init__(self, client: BaseClient):
        self.client = client

    def list_horizons(self) -> list[int]:
        return list(range(2025, 2100, 5))

    def list_pathways(self) -> list[str]:
        return [
            "SV",
            "ssp126",
            "ssp245",
            "ssp370",
            "ssp585",
            "<2 degrees",
            "2-3 degrees",
            "3-4 degrees",
            ">4 degrees",
        ]
