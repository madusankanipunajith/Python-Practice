def swap_case(ss):
    s = list(ss)
    for index, letter in enumerate(s):
        if letter.isupper():
            s[index] = letter.lower()

        elif letter.islower():
            s[index] = letter.upper()

        else:
            pass

    return ''.join(s)


output = swap_case('HackerRank.com presents "Pythonist 2".')
print(output)
