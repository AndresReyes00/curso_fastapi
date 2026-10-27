from pydantic import BaseModel, EmailStr, Field


class Transaction(BaseModel):
    id: int = Field(..., description="The unique identifier for the transaction")
    amount: float = Field(..., gt=0, description="The amount of the transaction, must be greater than 0")
    currency: str = Field(..., description="The currency of the transaction")
    timestamp: str = Field(..., description="The timestamp of when the transaction occurred")