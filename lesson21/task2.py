import unittest
from task1 import FileManager


class TestFileManager(unittest.TestCase):
    def test_writing_and_reading(self):
        filename = "test_file.txt"
        with FileManager(filename, "w") as file_manager:
            file_manager.write("Hello, World!")
            file_manager.write("This is a test.")

        with FileManager(filename, "r") as file_manager:
            content = file_manager.read()
            self.assertEqual(content, "Hello, World!This is a test.")

    def test_counter(self):
        filename = "test_counter.txt"
        with FileManager(filename, "w") as file_manager:
            file_manager.write("Line 1")
            file_manager.write("Line 2")

        self.assertEqual(file_manager.counter, 2)

    def test_error_handling(self):
        # Testing error handling when opening non-existent file
        with self.assertRaises(FileNotFoundError):
            with FileManager("nonexistent.txt", "r") as file_manager:
                pass

        # Testing error handling within the context
        filename = "test_error_handling.txt"
        with FileManager(filename, "w") as file_manager:
            file_manager.write("Test content")
            # Force an exception by dividing by zero
            with self.assertRaises(ZeroDivisionError):
                1 / 0

        # Ensure the file is still closed after the exception
        self.assertFalse(file_manager.file or file_manager.file.closed)

    def test_exit_message(self):
        filename = "test_exit_message.txt"
        with FileManager(filename, "w") as file_manager:
            file_manager.write("Test content")

        # Capture printed output
        from io import StringIO
        import sys
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        with FileManager(filename, "r") as file_manager:
            content = file_manager.read()

        exit_message = sys.stdout.getvalue().strip()
        sys.stdout = original_stdout

        expected_message = f"File '{filename}' was successfully processed."
        self.assertEqual(exit_message, expected_message)


if __name__ == "__main__":
    unittest.main()
