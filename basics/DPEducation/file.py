fhandler = open('file1.txt', 'r')
line_1 = fhandler.readline()
line_2 = fhandler.readline()

fhandler2 = open('file2.txt', 'w')
fhandler2.write(line_1 + line_2)
fhandler2.close()

fhandler2 = open('file2.txt', 'r')
print(fhandler2.read())

fhandler2.close()
fhandler.close()

