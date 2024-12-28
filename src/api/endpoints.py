import uvicorn
from fastapi import FastAPI

from src.api.routes import router_tables
from src.settings import settings


class CISTierAPI(FastAPI):
    def __init__(self) -> None:
        super().__init__(
            **settings.set_app_attributes
        )
        self._routers = [
            (router_tables, "/v1/tables")
        ]
        self._include_routes()

    def _include_routes(self) -> None:
        for router, prefix in self._routers:
            self.include_router(
                router,
                prefix=prefix
            )

    def run(self) -> None:
        uvicorn.run(app=self, port=8000, host="0.0.0.0")
