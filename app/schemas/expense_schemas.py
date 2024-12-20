from datetime import date
from app.schemas.payment_schemas import PaymentMethodResponse
from pydantic import BaseModel, Field, constr


class ExpenseBase(BaseModel):
    description: constr(min_length=3, max_length=255)  
    amount: float = Field(gt=0)                       
    category: constr(min_length=3, max_length=50)     
    date: date  
    payment_method_id: int

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int
    payment_method: PaymentMethodResponse

    class Config:
        orm_mode = True