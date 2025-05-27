import helper
from flask import Flask, request, render_template, redirect, url_for, Response

app = Flask(__name__)

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
