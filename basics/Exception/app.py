# Exception
print("Exceptions in python")

try:
    value = int(input("> "))
    print("Inside the try block")
    number = 100 / value
    print(number)
except ZeroDivisionError:
    print("can't divided by zero")
except ValueError:
    print("invalid error")

# Classes
text = "hello world"
print(text.capitalize())

num = input(":")

if float(num) < 0:
    raise ValueError("Negative!")




