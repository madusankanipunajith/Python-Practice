# Variables

name = "Madusanka Nipunajith"
age = 25
male = True

print("My name is ", name);
print("My age is ", int(age))
print("Hello world")

# Inputs
name = input("Your name ? ")
age = input("Your age ? ")
color = input("Your color ? ")

print(name + " is "+ age +" years old. He likes "+color)

# String

course = "Python's course for beginners"
another = course[:]
course_new = 'Python for "beginners"'
email = '''
Hi Madusanka,
How are you. Hope we can meet tomorrow.
Thank you.
'''

print(course)
print(another)
print(course_new)
print(email)
print(course[0])
print(course[-1])
print(course[0:])

# Including first index and excluding last index
print(course[1:3])
print(course[:5])

# Format method
first = "Madusanka"
last = "Nipunajith"
msg = f'{first} {last} is a software engineer'
print(msg)

# String method [len(), upper(), lower(), find()]
message = "Madusanka Nipunajith is a software engineer"
print(len(message))
print(message.upper())
print(message.lower())
# index of the first occurrence
print(message.find('M'))
print(message.find("software"))
new_message = message.replace("software", "civil")
print(new_message)
print(message.title())


