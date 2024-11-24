
#DONOT CHANGE THE CODE BELOW

from functions.library_system import initialize_database, add_book, search_book, list_books

def main():
    initialize_database()
    while True:
        print("\nLibrary System")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. List All Books")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            add_book(title, author)
            print(f"Book '{title}' by {author} added successfully!")
        elif choice == "2":
            title = input("Enter the title to search for: ")
            book = search_book(title)
            if book:
                print(f"Found: {book['title']} by {book['author']}")
            else:
                print("Book not found.")
        elif choice == "3":
            books = list_books()
            if books:
                print("Books in the library:")
                for book in books:
                    print(f"- {book['title']} by {book['author']}")
            else:
                print("No books in the library.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
