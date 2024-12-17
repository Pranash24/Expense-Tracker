from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.payment_schemas import PaymentMethodCreate, PaymentMethodResponse
from app.crud.payment_crud import create_payment_method, get_payment_methods

router = APIRouter()

@router.post("/payment-methods", response_model=PaymentMethodResponse)
def add_payment_method(payment_method: PaymentMethodCreate, db: Session = Depends(get_db)):
    return create_payment_method(db, payment_method)

@router.get("/payment-methods", response_model=list[PaymentMethodResponse])
def list_payment_methods(db: Session = Depends(get_db)):
    return get_payment_methods(db)
