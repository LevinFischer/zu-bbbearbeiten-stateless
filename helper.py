from dataclasses import dataclass
from datetime import datetime, date

# MUSS 'items' heißen, damit der Test funktioniert!
items = []

@dataclass
class Todo:
    title: str
    date: date
    isCompleted: bool = False
    description: str = ""  # Neues Feld
    category: str = "Allgemein"  # Neues Feld für Kategorie

def add(title, date_str, description=""):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    items.append(Todo(title, parsed_date, False, description, "Allgemein"))

def add_with_category(title, date_str, category):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    items.append(Todo(title, parsed_date, False, category))  # Mit Kategorie

def get_all():
    return items

def get(index):
    return items[index]

def update(index):
    items[index].isCompleted = not items[index].isCompleted
