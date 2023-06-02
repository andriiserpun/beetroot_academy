class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.log_file = "logs.txt"
    def log_error(self):
        with open(self.log_file, "a") as file:
            file.write(f"Error: {self.msg}")
try:
    raise CustomException("Error. Incorrect data")
except CustomException as e:
    print(e)
    e.log_error()