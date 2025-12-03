"""t = open('testdata.txt', 'r')
t = open('testdata.txt', 'w')
t = open('testdata.txt', 'r+')
t = open('testdata.txt', 'w+')
t = open('testdata.txt', 'b')
t.close()#automatically close"""

with open('testdata.txt', 'r') as file:
     data = file.read()


print(data)
