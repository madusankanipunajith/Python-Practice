input_list = input().split(" ")
input_list.sort()
count = 0

for i in range(1, int(input_list[0]) + 1):
    if int(input_list[0]) % i == 0 and int(input_list[1]) % i == 0:
        count += 1

print(count)
