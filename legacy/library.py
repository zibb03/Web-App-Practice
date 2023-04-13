books = {}

def add_book():
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Book ID already exists.")
        return
    book_name = input("Enter Book Name: ")
    publication_date = input("Enter Publication Date: ")
    publisher_name = input("Enter Publisher Name: ")
    publisher_phone_number = input("Enter Publisher Phone Number: ")
    author_name = input("Enter Author Name: ")
    author_email_address = input("Enter Author Email Address: ")
    books[book_id] = {
        "Book Name": book_name,
        "Publication Date": publication_date,
        "Publisher Name": publisher_name,
        "Publisher Phone Number": publisher_phone_number,
        "Author Name": author_name,
        "Author Email Address": author_email_address
    }
    print("Book added successfully.")

def update_book():
    book_id = input("Enter Book ID: ")
    if book_id not in books:
        print("Book ID does not exist.")
        return
    book_name = input("Enter Book Name: ")
    publication_date = input("Enter Publication Date: ")
    publisher_name = input("Enter Publisher Name: ")
    publisher_phone_number = input("Enter Publisher Phone Number: ")
    author_name = input("Enter Author Name: ")
    author_email_address = input("Enter Author Email Address: ")
    books[book_id] = {
        "Book Name": book_name,
        "Publication Date": publication_date,
        "Publisher Name": publisher_name,
        "Publisher Phone Number": publisher_phone_number,
        "Author Name": author_name,
        "Author Email Address": author_email_address
    }
    print("Book updated successfully.")

def delete_book():
    book_id = input("Enter Book ID: ")
    if book_id not in books:
        print("Book ID does not exist.")
        return
    del books[book_id]
    print("Book deleted successfully.")

def search_book():
    book_id = input("Enter Book ID: ")
    if book_id not in books:
        print("Book ID does not exist.")
        return
    print(books[book_id])

def display_books_by_author():
    author_name = input("Enter Author Name: ")
    for book_id, book in books.items():
        if book["Author Name"] == author_name:
            print(book_id, book)

def display_books_by_publisher():
    publisher_name = input("Enter Publisher Name: ")
    for book_id, book in books.items():
        if book["Publisher Name"] == publisher_name:
            print(book_id, book)

def display_all_books():
    for book_id, book in books.items():
        print(book_id, book)

while True:
    print("1. Add book information")
    print("2. Update book information")
    print("3. Delete book information")
    print("4. Search book information")
    print("5. Display a list of book(s) published by an author")
    print("6. Display a list of book(s) published by a publisher")
    print("7. Display a list of all book")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        display_books_by_author()
    elif choice == "6":
        display_books_by_publisher()
    elif choice == "7":
        display_all_books()
    elif choice == "8":
        break
    else:
        print("Invalid choice. Try again.")