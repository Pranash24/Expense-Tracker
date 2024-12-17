from sqlalchemy.orm import Session

from app.models.payment import PaymentMethod
from app.schemas.payment_schemas import PaymentMethodCreate

def create_payment_method(db: Session, payment_method: PaymentMethodCreate):
    db_payment_method = PaymentMethod(name=payment_method.name)
    db.add(db_payment_method)
    db.commit()
    db.refresh(db_payment_method)
    return db_payment_method

def get_payment_methods(db: Session):
    return db.query(PaymentMethod).all()
