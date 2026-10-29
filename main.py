from fastapi import FastAPI, HTTPException, status
from models.customer import Customer, CustomerCreate, CustomerUpdate
from models.invoice import Invoice
from models.transaction import Transaction
from db.connection import SessionDep, create_db_and_tables
from sqlmodel import select

app = FastAPI(lifespan=create_db_and_tables)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}



@app.get("/customers/", response_model=list[Customer], status_code=status.HTTP_200_OK)
async def get_customers(session: SessionDep): # type: ignore
    customers = session.exec(select(Customer)).all()
    return customers
    

@app.post("/customers/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerCreate, session: SessionDep): # type: ignore
    customer = Customer.model_validate(customer.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@app.get("/customer/{customer_id}", response_model=Customer, status_code=status.HTTP_200_OK)
async def get_customer(customer_id: int, session: SessionDep): # type: ignore
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer


@app.patch("/customer/{customer_id}", response_model=Customer, status_code=status.HTTP_202_ACCEPTED)
async def update_customer(customer_id: int, customer: CustomerUpdate, session: SessionDep): # type: ignore
    existing_customer = session.get(Customer, customer_id)
    if not existing_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")

    customer_data = customer.model_dump(exclude_unset=True)
    existing_customer.sqlmodel_update(customer_data)
    session.add(existing_customer)
    session.commit()
    session.refresh(existing_customer)

    return existing_customer


@app.delete("/customer/{customer_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_customer(customer_id: int, session: SessionDep): # type: ignore
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    
    session.delete(customer)
    session.commit()
    return None



@app.post("/transactions/", response_model=Transaction)
async def create_transaction(transaction: Transaction, session: SessionDep): # type: ignore
    transaction = Transaction.model_validate(transaction.model_dump())
    session.add(transaction)
    session.commit()
    session.refresh(transaction)
    return transaction


@app.post("/invoices/", response_model=Invoice)
async def create_invoice(invoice: Invoice, session: SessionDep): # type: ignore
    invoice = Invoice.model_validate(invoice.model_dump())
    session.add(invoice)
    session.commit()
    session.refresh(invoice)
    return invoice