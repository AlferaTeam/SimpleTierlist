from typing import List, Dict

from pydantic import BaseModel


class Tiers(BaseModel):
    sword: int
    netherite: int
    vanilla: int


class OverallPlayer(BaseModel):
    nickname: str
    points: int
    tiers: Tiers


class PaginatedResponse(BaseModel):
    status: str
    data: Dict[int, List[OverallPlayer]] = None
    details: str = None
