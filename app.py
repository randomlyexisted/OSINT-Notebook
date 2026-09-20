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

@app.route("/investigation/<int:investigation_id>")
def view_investigation(investigation_id):

    connection = get_db_connection()

    investigation = connection.execute("""
        SELECT *
        FROM investigations
        WHERE id = ?
    """, (investigation_id,)).fetchone()

    if investigation is None:
        connection.close()
        return "Investigation not found", 404

    people = connection.execute("""
        SELECT *
        FROM people
        WHERE investigation_id = ?
        ORDER BY created_at DESC
    """, (investigation_id,)).fetchall()

    connection.close()

    return render_template(
        "investigation.html",
        investigation=investigation,
        people=people
    )

@app.route("/investigation/<int:investigation_id>/people/new", methods=["GET", "POST"])
def create_person(investigation_id):
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]

        connection=get_db_connection()

        connection.execute("""
            INSERT INTO people (
                investigation_id,
                name,
                description
            )
            VALUES (?, ?, ?)
        """, (
            investigation_id, name, description
        ))

        connection.commit()
        connection.close()

        return redirect(url_for("view_investigation", investigation_id=investigation_id))

    connection = get_db_connection()
    investigation=connection.execute("""
        SELECT *
        FROM investigations
        WHERE id = ?
    """, (investigation_id,)).fetchone()

    if investigation is None:
        return "Investigation not found", 404

    return render_template(
        "create_person.html",
        investigation=investigation
    )


if __name__=="__main__":
    app.run(debug=True)