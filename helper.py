from datetime import datetime
import csv
import io
from database import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.Date)
    isCompleted = db.Column(db.Boolean, default=False)
    description = db.Column(db.String)
    category = db.Column(db.String, default="Allgemein")

def add(title, date_str, description=""):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    item = Todo(title=title, date=parsed_date, description=description)
    db.session.add(item)
    db.session.commit()

def add_with_category(title, date_str, category):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    item = Todo(title=title, date=parsed_date, category=category)
    db.session.add(item)
    db.session.commit()

def get_all():
    return Todo.query.all()

def get(index):
    return Todo.query.get(index)

def update(index):
    item = Todo.query.get(index)
    item.isCompleted = not item.isCompleted
    db.session.commit()

def get_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["title", "date", "isCompleted", "description", "category"])
    for item in Todo.query.all():
        writer.writerow([
            item.title,
            item.date.isoformat(),
            item.isCompleted,
            item.description,
            item.category
        ])
    return output.getvalue()
