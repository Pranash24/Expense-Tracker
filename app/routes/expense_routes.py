from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.expense_schemas import ExpenseCreate, ExpenseResponse, ExpenseUpdate
from app.crud.expense_crud import create_expense, get_expenses, get_statistics, delete_expense, update_expense
from app.database import get_db

router = APIRouter()
@router.get("/expenses")
def list_expenses(db: Session = Depends(get_db)):
    return get_expenses(db)
    
@router.post("/expenses/create", response_model=ExpenseResponse)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    if expense.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")
    return create_expense(db, expense)

@router.put("/expenses/{expense_id}", response_model=ExpenseResponse)
def update_expense_route(expense_id: int, updated_data: ExpenseUpdate, db: Session = Depends(get_db)):
    updated_expense = update_expense(db, expense_id, updated_data)
    if not updated_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated_expense

@router.delete("/expenses/{expense_id}")
def delete_expense_route(expense_id: int, db: Session = Depends(get_db)):
    success = delete_expense(db, expense_id)
    if not success:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"detail": "Expense deleted successfully"}

@router.get("/expenses/statistics")
def expenses_statistics(db: Session = Depends(get_db)):
    return get_statistics(db)


