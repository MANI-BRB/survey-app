# survey-app

A simple customer survey tool built with **Flask** and **SQLite**.

## Features
- Survey form with name + 3 questions
- Validation for required fields
- Responses persisted in SQLite (`survey.db`)
- Clients section with name + email storage
- Page to view all submitted survey responses
- Page to view all clients

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open: `http://127.0.0.1:5000`

## Routes
- `/` - Survey form
- `/thank-you` - Survey confirmation page
- `/responses` - List saved survey responses
- `/clients` - List clients
- `/clients/new` - Add a client
