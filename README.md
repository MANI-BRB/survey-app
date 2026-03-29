# survey-app

A simple survey web app built with **Flask** and **SQLite**.

## Features
- Survey form with name + 3 questions
- Validation for required fields
- Responses persisted in SQLite (`survey.db`)
- Page to view all submitted responses

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
- `/thank-you` - Confirmation page
- `/responses` - List saved responses
