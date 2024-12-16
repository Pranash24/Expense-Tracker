To run the API:

git clone https://github.com/Pranash24/Expense-Tracker.git

cd expense-tracker

python -m venv venv

venv\Scripts\activate #On Mac: source venv/bin/activate 

pip install -r requirements.txt

uvicorn app.main:app --reload


To test the API:

http://127.0.0.1:8000/docs#/
