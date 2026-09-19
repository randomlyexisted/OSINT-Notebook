from flask import Flask, render_template, request, redirect, url_for

from database import get_db_connection, initialize_database

app = Flask(__name__)

initialize_database()

@app.route("/")
def home():
    connection = get_db_connection()

    investigations = connection.execute("""
        SELECT *
        FROM investigations
        ORDER BY created_at DESC
    """).fetchall()

    connection.close()

    return render_template(
        "index.html",
        investigations=investigations
        )

@app.route("/investigation/new",methods=["GET", "POST"])
def create_investigation():
    if request.method=="POST":
        name = request.form["name"]
        description = request.form["description"]

        connection = get_db_connection()

        connection.execute("""
            INSERT INTO investigations (name, description)
            VALUES (?, ?)
        """, (name, description))
        connection.commit()
        connection.close()

        return redirect(url_for("home"))

    return render_template("create_investigation.html")


if __name__=="__main__":
    app.run(debug=True)