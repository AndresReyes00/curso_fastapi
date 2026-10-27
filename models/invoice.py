from pydantic import BaseModel, EmailStr, Field
from models.transaction import Transaction
from models.customer import Customer

class Invoice(BaseModel):
    id: int = Field(..., description="The unique identifier for the invoice")
    customer: Customer = Field(..., description="The customer associated with the invoice")
    transactions: list[Transaction] = Field(..., description="A list of transactions associated with the invoice") 
    total: float = Field(..., description="The total amount of the invoice, calculated from the transactions")


    @property
    def total_amount(self) -> float:
        """
        Calculate the total amount of the invoice by summing the amounts of all transactions.
        """
        return sum(transaction.amount for transaction in self.transactions)