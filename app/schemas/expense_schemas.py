from pydantic import BaseModel, Field, constr
from datetime import date

class ExpenseBase(BaseModel):
    description: constr(min_length=3, max_length=255)  
    amount: float = Field(gt=0)                       
    category: constr(min_length=3, max_length=50)     
    date: date  

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int

    class Config:
        orm_mode = True