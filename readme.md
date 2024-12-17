Expense Tracker API
Dit is een eenvoudige FastAPI-gebaseerde applicatie voor het beheren van je uitgaven. Met deze API kun je uitgaven toevoegen, bekijken, bijwerken, verwijderen en koppelen aan betalingsmethoden.

Installatie
Volg deze stappen om de API lokaal op te zetten:

1. Clone de repository
git clone https://github.com/Pranash24/Expense-Tracker.git
cd Expense-Tracker

3. Virtuele omgeving instellen

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
Code kopiëren
python -m venv venv
source venv/bin/activate

3. Installeer afhankelijkheden
Installeer de benodigde pakketten vanuit requirements.txt:
pip install -r requirements.txt

5. Start de applicatie
Draai de applicatie met Uvicorn:
uvicorn app.main:app --reload
De API draait nu lokaal op:
http://127.0.0.1:8000

API Testen
Gebruik de interactieve Swagger UI om de API te testen:
http://127.0.0.1:8000/docs

Voorbeeldroutes
Betalingsmethoden toevoegen
Endpoint: POST /api/payment-methods
Voorbeeld:

{ "name": "Credit Card" }
Uitgaven toevoegen
Endpoint: POST /api/expenses
Voorbeeld:
{
  "description": "Boodschappen",
  "amount": 45.50,
  "category": "Voeding",
  "date": "2024-12-17",
  "payment_method_id": 1
}
Uitgaven ophalen
Endpoint: GET /api/expenses

Projectstructuur
Expense-Tracker/
├── app/
│   ├── __init__.py
│   ├── main.py            # Startpunt van de applicatie
│   ├── models/            # Database modellen
│   ├── schemas/           # Pydantic schemas
│   ├── crud/              # CRUD-logica
│   ├── routes/            # API-routes
│   └── database.py        # Database setup
├── requirements.txt       # Benodigde Python-pakketten
└── README.md              # Documentatie
