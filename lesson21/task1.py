class FileManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.counter = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.counter = 0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        if exc_type is None:
            print(f"File '{self.filename}' was successfully processed.")
        else:
            print(f"An error occurred while processing file '{self.filename}': {exc_val}")

    def write(self, text):
        if self.file:
            self.counter += 1
            self.file.write(text)

    def read(self):
        if self.file:
            return self.file.read()
        return ""


filename = "example.txt"
with FileManager(filename, "w") as file_manager:
    file_manager.write("Hello, World!")
    file_manager.write("This is a test.")

with FileManager(filename, "r") as file_manager:
    content = file_manager.read()
    print(content)


print(f"Total write operations: {file_manager.counter}")
