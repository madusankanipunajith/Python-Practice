import math

name = "Madusanka"
print(name)
print(math.ceil(2.9))
print(math.floor(2.9))
print(math.gcd(7, 10))

# IF statement

is_hot = False
is_cold = False

if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
else:
    print("It is a lovely day")

print("Enjoy your day")

# Exersice

has_credit = True
cost = 1000000

if has_credit:
    print(int(cost * 0.1))
    down_payment = cost * 0.1
else:
    down_payment = cost * 0.2
    print(int(cost * 0.2))

print(f"down payment is ${down_payment}")

# Logical Operators (AND OR NOT)
good_gpa = True
good_heart = True

if good_gpa and good_heart:
    print("Good person")
else:
    print("Something has to be improved")

# Comparison Operators
name = input("Enter your name : ")
name_length = len(name)
if name_length < 3:
    print("Name is too short")
elif name_length > 50:
    print("Name is too long")
else:
    print("Looks good !")

# Weight converter (exercise)
weight = float(input("Enter value : "))
w_type = input("Enter type K(Kg) or L(lbs) : ")
convert_weight = 0.0

if w_type.lower() == 'k':
    convert_weight = weight * 2.2
    print(f"Lbs : {convert_weight}")
elif w_type.lower() == 'l':
    convert_weight = weight / 2.2
    print(f"Kgs : {convert_weight}")
else:
    print("something went wrong")
