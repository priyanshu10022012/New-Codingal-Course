file = open('Codingal.txt', 'r')
counter = 0

content = file.read()
CoList = content.split("\n")
print(CoList)
for i in CoList:
    if i:
        counter += 1
print(" This is the Number of lines in the file ")
print(counter)