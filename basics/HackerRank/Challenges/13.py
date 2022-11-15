s = str(input())
s_list = list(s)

for i in range(0, 5):
    if i == 0:
        for index, letter in enumerate(s_list):
            if letter.isalnum():
                print(True)
                break

            if index == len(s)-1:
                print(False)

    if i == 1:
        for index, letter in enumerate(s_list):
            if letter.isalpha():
                print(True)
                break

            if index == len(s) - 1:
                print(False)

    if i == 2:
        for index, letter in enumerate(s_list):
            if letter.isdigit():
                print(True)
                break

            if index == len(s) - 1:
                print(False)

    if i == 3:
        for index, letter in enumerate(s_list):
            if letter.islower():
                print(True)
                break

            if index == len(s) - 1:
                print(False)

    if i == 4:
        for index, letter in enumerate(s_list):
            if letter.isupper():
                print(True)
                break

            if index == len(s) - 1:
                print(False)

