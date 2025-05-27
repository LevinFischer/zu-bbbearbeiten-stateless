import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)


def test_add_with_category():
    # Vorbereitung: Leere Liste
    helper.items.clear()
    
    # Given: I want to add a to-do with a date and category
    text = "Kategorie-Test"
    date = "2025-05-27"
    category = "Schule"

    # When: I add the item with category
    helper.add_with_category(text, date, category)

    # Then: The item should have the correct category
    item = helper.items[-1]
    assert item.title == text.replace('b', 'bbb').replace('B', 'Bbb')
    assert isinstance(item.date, datetime.date)
    assert item.category == category
    assert item.isCompleted is False
