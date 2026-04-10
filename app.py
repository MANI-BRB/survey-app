from flask import Flask, g, redirect, render_template, request, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "survey.db"

QUESTIONS = [
    "How satisfied are you with our service?",
    "How likely are you to recommend us to a friend?",
    "What could we improve?",
]


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()

    db.executescript(

    db.execute(
 main
        """
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            q1 TEXT NOT NULL,
            q2 TEXT NOT NULL,
            q3 TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
 
        );

        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

        )
        """
    )
    db.execute(
    """
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    )
 main
    db.commit()


@app.route("/", methods=["GET", "POST"])
def survey():
    init_db()

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        answers = [request.form.get(f"q{i}", "").strip() for i in range(1, 4)]

        if not name or any(not a for a in answers):
            return render_template(
                "survey.html",
                questions=QUESTIONS,
                error="Please fill out your name and all questions.",
                previous={"name": name, "q1": answers[0], "q2": answers[1], "q3": answers[2]},
            )

        db = get_db()
        db.execute(
            "INSERT INTO responses (name, q1, q2, q3) VALUES (?, ?, ?, ?)",
            (name, answers[0], answers[1], answers[2]),
        )
        db.commit()
        return redirect(url_for("thank_you"))

    return render_template("survey.html", questions=QUESTIONS, error=None, previous={})


@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")


@app.route("/responses")
def responses():
    init_db()
    rows = get_db().execute(
        "SELECT name, q1, q2, q3, created_at FROM responses ORDER BY id DESC"
    ).fetchall()
    return render_template("responses.html", responses=rows)


@app.route("/clients")
def clients():
    init_db()
    rows = get_db().execute(
        "SELECT name, email, created_at FROM clients ORDER BY id DESC"
    ).fetchall()
    return render_template("clients.html", clients=rows)


@app.route("/clients/new", methods=["GET", "POST"])
def new_client():
    init_db()

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name or not email:
            return render_template(
                "new_client.html",
                error="Please fill out both name and email.",
                previous={"name": name, "email": email},
            )

        get_db().execute(
            "INSERT INTO clients (name, email) VALUES (?, ?)",
            (name, email),
        )
        get_db().commit()
        return redirect(url_for("clients"))

    return render_template("new_client.html", error=None, previous={})



 main
if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
