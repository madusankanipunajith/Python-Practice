# Inheritance
class Mamal:
    def walk(self):
        print("Walking the mamal")


class Dog(Mamal):
    def bark(self):
        print("Dog is barking")


class Cat(Mamal):
    def jump(self):
        print("Cat is jumping")


dog = Dog()
dog.bark()

cat = Cat()
cat.walk()
cat.jump()

# Modules
