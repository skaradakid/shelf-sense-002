import subprocess
import unittest
import os
from functions.library_system import DATABASE_FILE

class TestIntegrationLibrarySystem(unittest.TestCase):
    def setUp(self):
        """
        Set up a temporary database for integration testing.
        """
        self.test_db = "test_books.txt"
        global DATABASE_FILE
        DATABASE_FILE = self.test_db
        with open(self.test_db, 'w') as f:
            f.write("")  # Ensure the test database starts empty

    def tearDown(self):
        """
        Clean up after tests.
        """
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def run_main_with_input(self, user_input):
        """
        Simulate running the main.py script with user input.
        :param user_input: A string with simulated user inputs, separated by newlines.
        :return: The output of the script.
        """
        process = subprocess.Popen(
            ["python", "main.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output, _ = process.communicate(user_input)
        return output

    def test_add_and_list_books(self):
        """
        Test adding books and listing them.
        """
        user_input = "1\n1984\nGeorge Orwell\n1\nTo Kill a Mockingbird\nHarper Lee\n3\n4\n"
        output = self.run_main_with_input(user_input)
        self.assertIn("Book '1984' by George Orwell added successfully!", output)
        self.assertIn("Book 'To Kill a Mockingbird' by Harper Lee added successfully!", output)
        self.assertIn("Books in the library:", output)
        self.assertIn("1984 by George Orwell", output)
        self.assertIn("To Kill a Mockingbird by Harper Lee", output)

    def test_search_book(self):
        """
        Test searching for a book.
        """
        user_input = "1\n1984\nGeorge Orwell\n2\n1984\n4\n"
        output = self.run_main_with_input(user_input)
        self.assertIn("Book '1984' by George Orwell added successfully!", output)
        self.assertIn("Found: 1984 by George Orwell", output)

    def test_search_book_not_found(self):
        """
        Test searching for a book that doesn't exist.
        """
        user_input = "2\nNonexistent Book\n4\n"
        output = self.run_main_with_input(user_input)
        self.assertIn("Book not found.", output)

    def test_exit(self):
        """
        Test exiting the program.
        """
        user_input = "4\n"
        output = self.run_main_with_input(user_input)
        self.assertIn("Goodbye!", output)

if __name__ == "__main__":
    unittest.main()
