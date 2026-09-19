from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    investigations = [
        {
            "name": "Example Company",
            "description": "Sample investigation"
        },
        {
            "name": "Project Alpha",
            "description": "Research project"
        }
    ]

    return render_template(
        "index.html",
        investigations=investigations
        )
    return render_template("Index.html")

@app.route("/investigation/new")
def create_investigation():
    return render_template("create_investigation.html")

if __name__=="__main__":
    app.run(debug=True)