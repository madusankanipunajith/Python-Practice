def is_leap(_year):
    leap = False

    if (year % 400 == 0) and (year % 100 == 0):
        leap = True
    elif (year % 4 == 0) and (year % 100 != 0):
        leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))

