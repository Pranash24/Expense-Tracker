from pydantic import BaseModel
from datetime import date

class ExpenseBase(BaseModel):
    description: str
    amount: float
    category: str
    date: date

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int

    class Config:
        orm_mode = True
