class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __gt__(self, other):
        return True if self.__age > other.__age else False


roger = Dog('roger', 5)
syd = Dog('syd', 4)
print(roger > syd)
