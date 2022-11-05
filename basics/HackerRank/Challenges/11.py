def merge_the_tools(string, k):
    # your code goes here
    chunks = [string[i:i + k] for i in range(0, len(string), k)]
    for s in chunks:
        output = []
        for letter in s:
            if letter not in output:
                output.append(letter)
            else:
                pass
        for x in output:
            print(x, end='')
        print()


s = "madusanka nipunajith"


def solve(s):
    new_list = s.split(" ")
    output = ""
    for name in new_list:
        output = output + " " + name.capitalize()

    return output.strip()


# merge_the_tools('AABCAAADA', 3)

result = solve("madusanka nipunajith")
print(result)
