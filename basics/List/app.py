# append(), insert(), remove(), clear(), index(), count(), sort(), reverse(), copy()
# object in [] => return boolean value

numbers = [2, 40, 6, 7, 8, 34, 12, 88, 90]

numbers.sort()
print(numbers)
numbers.insert(0, 85)
print(numbers)
clone_numbers = numbers.copy()
numbers.reverse()
print(numbers)
numbers.remove(90)
print(numbers)

print(clone_numbers)

print(90 in numbers)

print(numbers.index(88))

count = numbers.count(2)
print(count)

print(numbers.pop())
print(numbers)

numbers.clear()
print(numbers)

# Exercise : remove duplicates in a list
initial_list = [12, 67, 89, 90, 90, 90, 55, 45, 55, 12, 67, 88, 1100, 567, 900]
for number in initial_list:
    count = initial_list.count(number)
    if count > 1:
        initial_list.remove(number)
else:
    print(initial_list)
