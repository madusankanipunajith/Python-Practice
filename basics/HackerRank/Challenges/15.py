x = int(input("x"))
y = int(input("y"))
z = int(input("z"))
n = int(input("n"))

my_list = []
new_list = []

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            my_list.append([i, j, k])


for index in range(0, len(my_list)):
    if sum(my_list[index]) == n:
        pass
    else:
        new_list.append(my_list[index])


print(new_list)

