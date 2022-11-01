# list set dict tuples

# list => hetoro... and mutable

dogs = ["Roger", "Syd", "Sha", 1, True]
print(1 in dogs)  # True
print(dogs[0], dogs[-1])
print(dogs.index("Sha"))
print(dogs[2:4])  # from 2 to 3 indexes which is starting from 0

dogs[2] = "Bow"
print(dogs)
print(len(dogs))

dogs.append("Judah")  # only one value
print(dogs)

dogs.extend(["Beau", 5])  # extend using list
print(dogs)

dogs += ["Black", "Rox"]
print(dogs)

dogs.remove("Bow")
print(dogs)

print(dogs.pop())
print(dogs)

dogs.insert(2, "Judo")
print(dogs)

cats = ["S", "P", "F", "G", "A"]
cats2 = ["S", "P", "F", "G", "H", "I", "A", "B"]
cats.sort()
print(cats)
cats.sort(key=str.lower)  # Do change in same variable
print(cats)

sorted(cats2, key=str.lower)  # It returns a new copy
print(cats2)

# tuples => immutable and hetoro...

names = ("Madusanka", "Nipunajith", "Roger", "Alex")
print(names[0])
print(len(names))
print(names.index("Roger"))
print(names[:len(names)])
print(sorted(names))
print(names)

# dictionary
dog = {"name": "Roger", "age": 10, "gender": "male", "color": "black"}
dog_copy = dog.copy()
print(dog_copy)
print(dog.get("name") + " "+ dog["name"])
print(dog.get("color", "brown"))
print(dog.pop("name"))
print(dog)
print(dog.popitem())
print(dog)
print("color" in dog)
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))
print(len(dog))
dog["food"] = "meat"
print(dog)
del dog["food"]
print(dog)

# sets


