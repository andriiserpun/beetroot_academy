import re
class MyClass:
    def __init__(self, email):
        self.email = email
    @classmethod
    def validate(cls, email):
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            raise ValueError("Invalid email address")
        print("Valid email address")

try:
    MyClass.validate("andrewserpun2001@gmail.com")
except ValueError as e:
    print("Error:", str(e))
