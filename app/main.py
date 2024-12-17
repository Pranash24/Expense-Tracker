from fastapi import FastAPI
from app.routes.expense_routes import router as expenses_router
from app.routes.payment_routes import router as payments_router
from app.database import init_db
from app.routes.expense_routes import router

app = FastAPI(title="Expense Tracker API")


app.include_router(expenses_router, prefix="/api")
app.include_router(payments_router, prefix="/api", tags=["Payment Methods"])


@app.on_event("startup")
def on_startup():
    init_db()
