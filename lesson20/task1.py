# в этом тесте я выбрал упражнение из 11 урока первого задания
import unittest

class FileManipulator:
    def write_to_file(self, filename, content):
        with open(filename, "w") as file:
            file.write(content)

    def read_from_file(self, filename):
        with open(filename, "r") as file:
            content = file.read()
        return content

class TestFileManipulator(unittest.TestCase):
    def setUp(self):
        self.file_manipulator = FileManipulator()
        self.filename = "test_file.txt"

    def tearDown(self):
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_and_read(self):
        content_to_write = "Testing file manipulation"
        self.file_manipulator.write_to_file(self.filename, content_to_write)
        content_read = self.file_manipulator.read_from_file(self.filename)
        self.assertEqual(content_to_write, content_read)

    def test_empty_file(self):
        empty_content = ""
        self.file_manipulator.write_to_file(self.filename, empty_content)
        content_read = self.file_manipulator.read_from_file(self.filename)
        self.assertEqual(empty_content, content_read)

if __name__ == '__main__':
    unittest.main()

