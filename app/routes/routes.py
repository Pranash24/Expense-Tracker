from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.schemas import ExpenseCreate, ExpenseResponse
from app.crud.crud import create_expense, get_expenses
from app.database import get_db

router = APIRouter()

@router.post("/expenses", response_model=ExpenseResponse)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return create_expense(db, expense)

@router.get("/expenses")
def list_expenses(db: Session = Depends(get_db)):
    return get_expenses(db)
