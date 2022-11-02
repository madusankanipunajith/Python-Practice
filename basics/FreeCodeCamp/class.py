# modules

class Dog:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def bark(self):
        print("Woof!")


# Lambda functions

res = lambda num: num * 2
multiply = lambda a, b: a * b
print(multiply(2, 3))
print(res(6))

# map, filter, reduce

