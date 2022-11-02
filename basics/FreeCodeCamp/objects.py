# objects => everything in python is an object

age = 45
print(age.real)
print(age.imag)
print(age.bit_length())

items = [1, 2, 3]
items.pop()
print(id(items))

# Loops => while and for loops

count = 0
while count < 10:
    print(count)
    count += 1

for i in items:
    print(i)

for i in range(15):
    print(i)

items2 = [1, 2, 3, 4]
for index, item in enumerate(items2):
    print(index, item)


# continue and break
for item in items2:
    if item == 2:
        continue
    print(item)

