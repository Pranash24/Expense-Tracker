from sqlalchemy.orm import Session
from app.models.Expense import Expense
from app.schemas.schemas import ExpenseCreate

def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session):
    return db.query(Expense).all()

def get_statistics(db: Session):
    expenses = db.query(Expense).all()
    total = sum(exp.amount for exp in expenses)
    by_category = {}
    for exp in expenses:
        by_category[exp.category] = by_category.get(exp.category, 0) + exp.amount
    return {"total": total, "by_category": by_category}
