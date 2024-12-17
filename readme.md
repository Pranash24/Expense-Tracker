Expense Tracker API

Projectomschrijving: De Expense Tracker API is een backend applicatie gebouwd met FastAPI. Het stelt gebruikers in staat om uitgaven te beheren, inclusief functionaliteiten zoals het toevoegen, bekijken, bijwerken en verwijderen van uitgaven. Daarnaast kunnen gebruikers hun uitgaven filteren per categorie of betaalmethode.

Installatie-instructies:

1. Clone de repository:

git clone https://github.com/Pranash24/Expense-Tracker.git

cd Expense-Tracker

3. Maak een virtuele omgeving:

3A. Windows:

python -m venv venv

venv\Scripts\activate

3B. Mac/Linux:

python -m venv venv

source venv/bin/activate

4. Installeer de afhankelijkheden:

pip install -r requirements.txt

5. Start de server:

uvicorn app.main:app --reload

6. Ga naar de API-documentatie: Open de volgende URL in je browser:

http://127.0.0.1:8000/docs#/
