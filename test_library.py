from library import add_book, issue_book, return_book
from data import library_books, issued_books

def reset_data():
    library_books.clear()
    issued_books.clear()

def test_add_book():
    reset_data()
    assert add_book("Python Basics") is True

def test_issue_book():
    reset_data()
    add_book("Python Basics")
    assert issue_book("Python Basics", "Sujal") is True

def test_return_book():
    reset_data()
    add_book("Python Basics")
    issue_book("Python Basics", "Sujal")
    assert return_book("Python Basics") is True
