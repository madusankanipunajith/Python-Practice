def hello(name="Madusanka", age=25):
    print("Hello " + name)
    print("You are " + str(age) + " years old")


hello(age=34)
hello("Roger")
hello("Nipunajith", 29)


def change(value):
    value["name"] = "Madusanka"


# dict are mutable
val = {"name": "Nipunajith"}
print(val)
change(val)
print(val)


def hello2(name):
    if not name:
        return

    return "HI " + name


print(hello())
print(hello2("Madusanka"))


# nested functions

def talk(phrase):
    def say(_word):
        print(_word)

    words = phrase.split(' ')
    for word in words:
        say(word)


talk("Hello My name is Madusanka")


def count():
    counts: int = 0

    def increment():
        nonlocal counts
        counts+=1
        print(counts)

    increment()


count()


