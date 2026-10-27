from fastapi import FastAPI
from models.customer import Customer, CustomerCreate
from models.invoice import Invoice
from models.transaction import Transaction


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


db_customer = []

@app.get("/customers/", response_model=list[Customer])
async def get_customers():
    return db_customer


@app.post("/customers/", response_model=Customer)
async def create_customer(customer: CustomerCreate):

    customer = Customer.model_validate(customer.model_dump())
    customer.id= len(db_customer) + 1
    db_customer.append(customer)

    return customer






@app.post("/transactions/", response_model=Transaction)
async def create_transaction(transaction: Transaction):
    return {"message": "Transaction created successfully", "transaction": transaction}


@app.post("/invoices/", response_model=Invoice)
async def create_invoice(invoice: Invoice):
    return {"message": "Invoice created successfully", "invoice": invoice}