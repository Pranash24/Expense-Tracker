from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.expense_schemas import ExpenseCreate, ExpenseResponse, ExpenseUpdate
from app.crud.expense_crud import create_expense, get_expenses, get_statistics, delete_expense, update_expense, get_filtered_expenses
from app.database import get_db

router = APIRouter()
@router.get("/expenses",tags=["CRUD Expenses"])
def list_expenses(db: Session = Depends(get_db)):
    return get_expenses(db)
    
@router.post("/expenses/create", response_model=ExpenseResponse,tags=["CRUD Expenses"])
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    if expense.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")
    return create_expense(db, expense)

@router.put("/expenses/{expense_id}", response_model=ExpenseResponse,tags=["CRUD Expenses"])
def update_expense_route(expense_id: int, updated_data: ExpenseUpdate, db: Session = Depends(get_db)):
    updated_expense = update_expense(db, expense_id, updated_data)
    if not updated_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated_expense

@router.delete("/expenses/{expense_id}",tags=["CRUD Expenses"])
def delete_expense_route(expense_id: int, db: Session = Depends(get_db)):
    success = delete_expense(db, expense_id)
    if not success:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"detail": "Expense deleted successfully"}

@router.get("/expenses/statistics",tags=["Expenses Data"])
def expenses_statistics(db: Session = Depends(get_db)):
    return get_statistics(db)

@router.get("/expenses/search",tags=["Expenses advanced search"])
def list_expenses_search(
    db: Session = Depends(get_db),
    category: str = Query(None, description="Filter by category"),
    start_date: str = Query(None, description="Filter by start date (YYYY-MM-DD)"),
    end_date: str = Query(None, description="Filter by end date (YYYY-MM-DD)"),
    search: str = Query(None, description="Search by description"),
    min_amount: float = Query(None, description="Filter by minimum amount"),
    max_amount: float = Query(None, description="Filter by maximum amount"),
):
    return get_filtered_expenses(
        db=db,
        category=category,
        start_date=start_date,
        end_date=end_date,
        search=search,
        min_amount=min_amount,
        max_amount=max_amount,
    )
