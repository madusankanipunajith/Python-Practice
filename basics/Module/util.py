def find_max(lis):
    max_val = lis[0]
    for value in lis:
        if max_val < value:
            max_val = value

    return max_val


