# survey-app

codex/create-a-simple-survey-web-app-p7anze
A simple customer survey tool built with **Flask** and **SQLite**.

A simple survey web app built with **Flask** and **SQLite**.
main

## Features
- Survey form with name + 3 questions
- Validation for required fields
- Responses persisted in SQLite (`survey.db`)
codex/create-a-simple-survey-web-app-p7anze
- Clients section with name + email storage
- Page to view all submitted survey responses
- Page to view all clients

- Page to view all submitted responses
main

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
codex/create-a-simple-survey-web-app-p7anze
- `/thank-you` - Survey confirmation page
- `/responses` - List saved survey responses
- `/clients` - List clients
- `/clients/new` - Add a client

- `/thank-you` - Confirmation page
- `/responses` - List saved responses
 main
