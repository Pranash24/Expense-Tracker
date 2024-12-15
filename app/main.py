from fastapi import FastAPI
from app.routes.expense_routes import router
from app.database import init_db


app = FastAPI(title="Expense Tracker API")


app.include_router(router)


@app.on_event("startup")
def on_startup():
    init_db()
