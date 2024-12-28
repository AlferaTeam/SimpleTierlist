from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status: str
    data: None
    details: str
