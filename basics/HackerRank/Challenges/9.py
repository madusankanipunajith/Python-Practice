from collections import Counter

X = int(input())
list_of_shoes = list(map(int, input().split()))
N = int(input())
transaction = []
total = 0

dict_list_of_shoes = Counter(list_of_shoes)

for i in range(N):
    inp = list(map(int, input().split()))
    transaction.append(inp)

for i in transaction:
    if i[0] in dict_list_of_shoes.keys() and dict_list_of_shoes[i[0]] > 0:
        total += i[1]
        dict_list_of_shoes[i[0]] -= 1
    else:
        pass


print(total)
