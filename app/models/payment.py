from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base 

class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    expenses = relationship("Expense", back_populates="payment_method")
