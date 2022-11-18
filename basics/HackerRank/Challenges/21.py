from itertools import combinations_with_replacement

inp = input().split(" ")
s = inp[0]
n = int(inp[1])
str_list = []


sorted_s = sorted(list(s))

per_list = list(combinations_with_replacement(sorted_s, n))

for item in per_list:
    _str = ''.join(item)
    str_list.append(_str)

for i in str_list:
    print(i)

