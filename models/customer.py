from pydantic import BaseModel, EmailStr, Field



class CustomerBase(BaseModel):
    name: str = Field(..., description="The name of the customer")
    email: EmailStr = Field(..., description="The email address of the customer")
    age : int = Field(..., gt=0, description="The age of the customer, must be greater than 0")


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int | None = Field(None, description="The unique identifier for the customer")