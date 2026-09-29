from src.data import library_books, issued_books
def add_book(title):
    if title not in library_books:
        library_books.append(title)
        return True
    return False

def issue_book(title, student):
    if title in library_books and title not in issued_books:
        issued_books[title] = student
        return True
    return False

def return_book(title):
    if title in issued_books:
        issued_books.pop(title)
        return True
    return False

def get_books():
    return library_books
