import os
from flask import Flask, request, render_template, redirect, url_for, Response
from dotenv import load_dotenv
from database import db
import helper

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}".format(
    dbuser=os.environ["DBUSER"],
    dbpass=os.environ["DBPASS"],
    dbhost=os.environ["DBHOST"],
    dbname=os.environ["DBNAME"]
)
db.init_app(app)
app.app_context().push()
db.create_all()

@app.route("/")
def index():
    todos = helper.get_all()
    return render_template('index.html', items=todos)

@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("text")
    date = request.form.get("date")
    description = request.form.get("description")
    helper.add(title, date, description)
    return redirect(url_for("index"))

@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))

@app.route("/download")
def get_csv():
    return Response(
        helper.get_csv(),
        mimetype="text/csv",
        headers={"Content-disposition":"attachment; filename=zu-bbbearbeiten.csv"},
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0")
