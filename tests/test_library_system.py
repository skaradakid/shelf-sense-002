import unittest
import os
from functions.library_system import initialize_database, add_book, search_book, list_books, DATABASE_FILE

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        """
        Setup a temporary database file for testing.
        """
        self.test_db = "test_books.txt"
        global DATABASE_FILE
        DATABASE_FILE = self.test_db
        initialize_database()
        # Clear test database
        with open(self.test_db, 'w') as f:
            f.write("")

    def tearDown(self):
        """
        Remove the test database file.
        """
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_book(self):
        """
        Test adding a new book to the library.
        """
        add_book("1984", "George Orwell")
        with open(self.test_db, 'r') as f:
            content = f.read()
        self.assertIn("1984,George Orwell", content)

    def test_search_book(self):
        """
        Test searching for a book in the library.
        """
        add_book("1984", "George Orwell")
        result = search_book("1984")
        self.assertIsNotNone(result)
        self.assertEqual(result['title'], "1984")
        self.assertEqual(result['author'], "George Orwell")

    def test_list_books(self):
        """
        Test listing all books in the library.
        """
        add_book("1984", "George Orwell")
        add_book("To Kill a Mockingbird", "Harper Lee")
        books = list_books()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0]['title'], "1984")
        self.assertEqual(books[1]['title'], "To Kill a Mockingbird")

if __name__ == "__main__":
    unittest.main()
