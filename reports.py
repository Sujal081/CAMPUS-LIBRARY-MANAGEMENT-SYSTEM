from src.data import library_books, issued_books
def show_books():
    print("\nLibrary Books:")

    if not library_books:
        print("No books in library.")
        return

    for book in library_books:
        if book in issued_books:
            print("-", book, "(Issued to", issued_books[book] + ")")
        else:
            print("-", book, "(Available)")

def show_summary():
    total=len(library_books)
    issued=len(issued_books)
    available=total-issued

    print("\nLibrary Summary")
    print("Total Books:", total)
    print("Issued Books:", issued)
    print("Available Books:", available)
