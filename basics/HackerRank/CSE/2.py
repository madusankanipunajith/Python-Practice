T = int(input())
first_list = []
second_list = []


def max_sum(arr, k):
    sum_res = 0
    sorted_arr = sorted(arr, reverse=True)
    for val in range(0, k):
        sum_res += sorted_arr[val]

    return sum_res


for i in range(0, T):
    input_1 = input("1 :").split()
    fl = [int(x) for x in input_1]
    input_2 = input("2 :").split()
    sl = [int(x) for x in input_2]
    first_list.append(fl)
    second_list.append(sl)

for i in range(0, T):
    print(max_sum(second_list[i], first_list[i][1]))


