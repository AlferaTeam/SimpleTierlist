from pydantic import BaseModel


class UserTierResponse(BaseModel):
    nickname: str
    tier: str
