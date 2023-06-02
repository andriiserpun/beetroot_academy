
class Person:
    def __init__(self, firstname, age):
        self.firstname = firstname
        self.age = age
    def introduce(self):
        print(f"Hello, my name is {self.firstname } and I'm {self.age} years old.")

    def greetings(self):
        print("Nice to meet you")

class Student(Person):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def introduce(self):
        print(f"Hi, my name is {self.firstname} {self.lastname}, I'm {self.age}.")
class Teacher(Person):
    def __init__(self, firstname, lastname, subject):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject
    def introduce(self):
        print(f"Good morning! My name is {self.firstname} {self.lastname}, I'm teaching {self.subject}.")

p = Person("Yuriy", 48)
p.introduce()
p.greetings()
print("______")
s = Student("Sergey", "Makushkin", 18)
s.introduce()
s.greetings()
print("______")
t = Teacher("Marina", "Vladimirovna", "English")
t.introduce()
t.greetings()