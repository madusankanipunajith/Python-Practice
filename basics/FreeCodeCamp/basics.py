# second session of the tutorial
from enum import Enum

name = "Madusanka"
is_married = False
long = 12.4

print(type(name))  # int float str bool
print(type(is_married))
print(isinstance(name, str))
print(str(long))

# casting => str to int , int to str, int to float, float to int
# data types (10) => complex, bool, int, str, float, list, tuple, set, dict, range
# operators (7) => arithmatic, logical, assignment, boolean, identity, membership, comparison

# multi line print
print("""
My name is Madusanka
I live in Gampaha
I am 25 years old
""")

# str inbuilt methods => lower(), upper(), islower(), isupper(), title(), startswith(), endswith(), replace(), strip(),
# split(), join(), find()
print("MaduSanka Nipunajith".lower())
print("MaduSanka Nipunajith".title())
print("MaduSanka Nipunajith".startswith("San"))

name = "Madusanka Nipunajith"
company = "WSO2,\"Sri Lanka\""
print(name.lower())
print(name)
print(len(name))
print("du" in name)
print(company)

# slicing
print(name[2:3])
print(name[3:])  # from 3 to end
print(name[:10])  # from 0 to 9

# any method, all method
ingredient_purchase = True
meal_cooked = False

result = any([ingredient_purchase, meal_cooked])
print(result)
result2 = all([ingredient_purchase, meal_cooked])
print(result2)

# complex numbers
num1 = complex(2, 3)
print(str(num1.real) + " " + str(num1.imag))

# abs and round
print(abs(-5.5))
print(round(12.4))


# enum => this is the only way to define constant in python
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE.value)
print(len(State))

