import helper
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    todos = helper.get_all()
    return render_template('index.html', items=todos)

@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("text")
    date = request.form.get("date")
    helper.add(title, date)
    return redirect(url_for("index"))

@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))
