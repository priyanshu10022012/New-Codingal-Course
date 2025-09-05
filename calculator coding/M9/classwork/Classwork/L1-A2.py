file_read = open('Codingal.txt', 'r')
print("File in Read more -")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in Write mode ....")
file_write.write("Hello, I am Priyanshu. I am 13 yr. old")
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("\n File in Append mode ....")
file_append.write("Hello, I am Priyanshu. I am 13 yr. old")
file_append.close()