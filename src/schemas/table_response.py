from typing import List, Dict

from pydantic import BaseModel


class TierPlayer(BaseModel):
    nickname: str
    region: str


class TierGroup(BaseModel):
    high: List[TierPlayer]
    low: List[TierPlayer]


class TiersResponse(BaseModel):
    tiers: Dict[int, TierGroup]

    class Config:
        json_schema_extra = {
            "example": {
                "tiers": {
                    1: {
                        "high": [
                            {"nickname": "Alice", "region": "US"}
                        ],
                        "low": [
                            {"nickname": "Bob", "region": "EU"}
                        ]
                    },
                    2: {
                        "high": [],
                        "low": []
                    }
                }
            }
        }
