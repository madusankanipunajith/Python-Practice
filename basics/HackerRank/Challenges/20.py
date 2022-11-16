from itertools import combinations

inp = input().split(" ")
s = inp[0]
n = int(inp[1])
str_list = []
per_list = []

sorted_s = sorted(list(s))

for i in range(1, n+1):
    _list = list(combinations(sorted_s, i))
    per_list.append(_list)


for item in per_list:
    for nested_item in item:
        str_list.append(''.join(nested_item))


for i in str_list:
    print(i)
