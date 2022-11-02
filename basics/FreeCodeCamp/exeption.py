try:
    result = 2 / 0
except EOFError:
    print("End of file error")
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("No exception is occurred")
finally:
    result = 1

try:
    raise Exception('An error!')
except Exception as error:
    print(error)


# custom exception
class DogNotFoundException(Exception):
    print("inside")
    pass


try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found")

print(result)


# with
with open('', 'r') as file:
    content = file.read()
    print(content)

