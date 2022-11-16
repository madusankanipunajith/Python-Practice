from itertools import product

x = input().split(" ")
y = input().split(" ")

resx = [eval(i) for i in x]
resy = [eval(i) for i in y]

XY = list(product(resx, resy))

print(XY)
