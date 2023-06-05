class Animal:
    def talk(self):
        pass
class Cat(Animal):
    def talk(self):
        return "miew"
class Dog(Animal):
    def talk(self):
        return "woof"
def animal_say_hello(animal):
    print(animal.talk())

cat = Cat()
dog = Dog()
animal_say_hello(cat)
animal_say_hello(dog)