class Dog:
    age_fuctor = 7
    def __init__(self, age_of_dog):
        self.age_of_dog = age_of_dog
    def human_age(self):
        return self.age_of_dog * self.age_fuctor
my_dog = Dog(3)
human_equiqalent_age = my_dog.human_age()
print(human_equiqalent_age)