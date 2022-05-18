# Tuples

coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)
print(y)
print(z)

my_list = [1, 3, 5, 7, 9, 3, 6]
print(my_list[5:1:-1])
print(my_list[1:5])

lists = [1, 1, 2, 3, 5, 8, 13]
print(lists[lists[4]])

str_1 = "cricket, "
print(str_1.join(["hello, world"]))

# Dictionaries
phone = {
    1: "one",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"
}

number = input("Phone: ")
for num in number:
    numeric_number = int(num)
    print(phone.get(numeric_number, "Default value as none"), end=" ")


