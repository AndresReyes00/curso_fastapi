from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class CustomerBase(SQLModel):
    name: str = Field(default=None, description="The name of the customer")
    email: EmailStr = Field(default=None, description="The email address of the customer")
    age : int = Field(default=None, gt=0, description="The age of the customer, must be greater than 0")


class CustomerCreate(CustomerBase):
    pass


    class Config:
        json_schema_extra = {
            "example": {
                "name": "JimcostDev",
                "email": "email@test.com",
                "age": 25
            }
        }


class CustomerUpdate(CustomerBase):
    pass


    class Config:
        json_schema_extra = {
            "example": {
                "name": "JimcostDev",
                "email": "email@test.com",
                "age": 25
            }
        }


class Customer(CustomerBase,table=True):
    id: int | None = Field(default=None, primary_key=True, description="The unique identifier for the customer")