from library import add_book, issue_book, return_book
from validators import valid_title, valid_student
from reports import show_books, show_summary
def run_library_system():
    while True:
        print("\nCampus Library Management System")
        print("1.Add Book")
        print("2.Issue Book")
        print("3.Return Book")
        print("4.Show Books")
        print("5.Show Summary")
        print("6.Exit")

        choice=input("Enter choice: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()

            if valid_title(title):
                if add_book(title):
                    print("Book added successfully.")
                else:
                    print("Book already exists.")
            else:
                print("Title cannot be empty.")

        elif choice == "2":
            title = input("Enter book title: ").strip()
            student = input("Enter student name: ").strip()

            if valid_title(title) and valid_student(student):
                if issue_book(title, student):
                    print("Book issued successfully.")
                else:
                    print("Book not available for issue.")
            else:
                print("Book title and student name cannot be empty.")

        elif choice == "3":
            title = input("Enter book title: ").strip()

            if return_book(title):
                print("Book returned successfully.")
            else:
                print("Book is not currently issued.")

        elif choice == "4":
            show_books()

        elif choice == "5":
            show_summary()

        elif choice == "6":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run_library_system()
