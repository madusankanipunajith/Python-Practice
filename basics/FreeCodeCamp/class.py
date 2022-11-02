# modules
from functools import reduce


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
numbers = [1, 2, 3, 4, 5, 6]

# def double(val):
#     return 2 * val

double = lambda val: 2 * val

results = map(double, numbers)
results_copy = map(lambda a: a * 2, numbers)

print(list(results))
print(list(results_copy))


def isEven(num):
    return num % 2 == 0


even_result = filter(isEven, numbers)
even_result_copy = filter(lambda a: a % 2 == 0, numbers)
print(list(even_result))
print(list(even_result_copy))

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]
_sum = 0
for expense in expenses:
    _sum += expense[1]

print(_sum)

_sum2 = reduce(lambda a, b: a[1] + b[1], expenses)
print(_sum2)
