import numpy as np

lists = []

axis = list(map(int, input().split()))

for i in range(0, int(axis[0])):
    my_list = list(map(int, input().split()))
    lists.append(my_list)

print(max(lists))
