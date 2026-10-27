from fastapi import FastAPI
from models import customer
from models.customer import Customer, CustomerCreate
from models.invoice import Invoice
from models.transaction import Transaction
from db.connection import session_dependency, create_db_and_tables
from sqlmodel import select

app = FastAPI(lifespan=create_db_and_tables)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}



@app.get("/customers/", response_model=list[Customer])
async def get_customers(session=session_dependency):
    customers = session.exec(select(Customer)).all()
    return customers


@app.post("/customers/", response_model=Customer)
async def create_customer(customer: CustomerCreate, session=session_dependency):
    customer = Customer.model_validate(customer.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@app.post("/transactions/", response_model=Transaction)
async def create_transaction(transaction: Transaction):
    return {"message": "Transaction created successfully", "transaction": transaction}


@app.post("/invoices/", response_model=Invoice)
async def create_invoice(invoice: Invoice):
    return {"message": "Invoice created successfully", "invoice": invoice}