from itertools import permutations
inp = input().split(" ")
s = inp[0]
n = int(inp[1])
str_list = []

per_list = list(permutations(s, n))

for item in per_list:
    str_list.append(''.join(item))

str_list.sort()
for string in str_list:
    print(string)
