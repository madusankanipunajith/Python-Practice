file = open("text.txt", "r")
print(file.read())
file.close()

# Valuable functions
numbers = [55, 67, 89, 90, 99, 89]

if all([i > 50 for i in numbers]):
    print('All are greater than 50')

print([i > 50 for i in numbers])

