from fastapi import APIRouter, HTTPException

from src.crud import (
    VanillaTierService,
    SwordTierService,
    NetheriteTierService
)
from src.schemas import (
    TiersResponse,
    ErrorResponse
)

router = APIRouter()

TABLE_SERVICES = {
    "sword": SwordTierService,
    "netherite": NetheriteTierService,
    "vanilla": VanillaTierService,
}


@router.get("/{table}", response_model=TiersResponse, responses={404: {"model": ErrorResponse}})
async def get_table(table: str) -> TiersResponse:
    service = TABLE_SERVICES.get(table)
    if service is None:
        raise HTTPException(
            status_code=404,
            detail=f"Table '{table}' does not exist."
        )

    response_table = await service.get_tiers()
    if response_table is None:
        raise HTTPException(
            status_code=404,
            detail=f"No data found for table '{table}'."
        )
    return response_table
