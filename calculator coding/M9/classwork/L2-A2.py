file = open('Codingal.txt', 'r')
print("Reading the file...")
print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("Reading the multiple lines...")
for i in range(3):
    print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("Looping through the lines...")
for line in file:
    print(line)
file.close()