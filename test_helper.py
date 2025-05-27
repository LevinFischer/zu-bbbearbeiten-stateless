import pytest
import datetime
import helper
from flask import Flask
from database import db
from helper import Todo

@pytest.fixture(scope="module", autouse=True)
def app_context():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # In-Memory DB für Tests
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
        yield
        db.drop_all()

def clear_db():
    db.session.query(Todo).delete()
    db.session.commit()

def test_add():
    clear_db()

    text = "Lorem ipsum"
    date = "2023-09-02"

    helper.add(text, date)

    item = Todo.query.order_by(Todo.id.desc()).first()
    assert isinstance(item.date, datetime.date)

def test_add_with_category():
    clear_db()

    text = "Kategorie-Test"
    date = "2025-05-27"
    category = "Schule"

    helper.add_with_category(text, date, category)

    item = Todo.query.order_by(Todo.id.desc()).first()
    assert item.title == text.replace('b', 'bbb').replace('B', 'Bbb')
    assert isinstance(item.date, datetime.date)
    assert item.category == category
    assert item.isCompleted is False

def test_get_csv():
    clear_db()

    helper.add("Test-Todo", "2025-05-27", "Testbeschreibung")

    # Kategorie manuell setzen
    item = Todo.query.order_by(Todo.id.desc()).first()
    item.category = "Testkategorie"
    db.session.commit()

    csv_output = helper.get_csv()

    lines = csv_output.strip().splitlines()
    assert lines[0] == "title,date,isCompleted,description,category"
    assert "Test-Todo" in lines[1]
    assert "Testbeschreibung" in lines[1]
    assert "Testkategorie" in lines[1]
