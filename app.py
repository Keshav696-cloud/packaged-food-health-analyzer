from flask import Flask, render_template
import sys
import os

# Let Python find build_database.py inside the database/ folder
sys.path.append(os.path.join(os.path.dirname(__file__), "database"))
import build_database  # type: ignore

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Auto-sync the database from Excel every time the server starts
    os.chdir(os.path.join(os.path.dirname(__file__), "database"))
    build_database.ensure_synced()
    os.chdir(os.path.dirname(__file__))

    app.run(debug=True)