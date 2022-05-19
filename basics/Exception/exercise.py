# Classes - Exercise
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Dog:
    def walk(self):
        print("Walking the dog")


class Cat:
    def walk(self):
        print("Walking the cat")


dog = Dog()
dog.walk()

cat = Cat()
cat.walk()
