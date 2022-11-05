vowels = ['A', 'E', 'I', 'O', 'U']


def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


def stuart(string):
    list_of_string = list(string)
    total = 0
    occur_list = []
    for (index, letter) in enumerate(list_of_string):
        if letter not in vowels:
            substring = string[index:]
            for sub_index in range(len(substring)):
                occur = substring[0:sub_index + 1]
                if occur not in occur_list:
                    # print(occur, occurrences(substring, occur))
                    total += occurrences(substring, occur)
                    occur_list.append(occur)
        else:
            pass

    return total


def kevin(string):
    list_of_string = list(string)
    total = 0
    occur_list = []
    for (index, letter) in enumerate(list_of_string):
        if letter in vowels:
            substring = string[index:]
            for sub_index in range(len(substring)):
                occur = substring[0:sub_index + 1]
                if occur not in occur_list:
                    # print(occur, occurrences(substring, occur))
                    total += occurrences(substring, occur)
                    occur_list.append(occur)
        else:
            pass

    return total


def minion_game(string):
    kevin_result = kevin(string)
    stuart_result = stuart(string)

    if stuart_result >= kevin_result:
        print(f"Stuart {stuart_result}")
    else:
        print(f"Kevin {kevin_result}")


minion_game("BANANA")



