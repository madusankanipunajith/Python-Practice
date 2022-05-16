numbers = [12, 45, 78, 90, 156, 40]

value = numbers[0]
max_value = value
for number in numbers:
    if number >= max_value:
        max_value = number
else:
    print(f"Max value is {max_value}")


# 2D List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

print(matrix[0][1])

