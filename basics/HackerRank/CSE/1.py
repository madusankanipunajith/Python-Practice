T = int(input())
number_list = []

for i in range(0, T):
    number = int(input(f"{i+1} : "))
    number_list.append(number)


def p_sum(num: int):
    count = 0
    for num_i in range(num + 1):
        count += num_i

    return count


def p_prod(num: int):
    count = 1
    for num_i in range(1, num + 1):
        count *= num_i

    return count


for number in number_list:
    if p_prod(number) % p_sum(number) == 0:
        print("YEAH")
    else:
        print("NAH")
