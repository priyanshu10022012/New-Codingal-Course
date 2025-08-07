a = 0
b = 1
print(a)
print(b)
for i in range(10):
    c = a + b
    print(c)
    a = b
    b = c
# This code prints the first 10 numbers in the Fibonacci sequence.
# The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
# The output will be:   0 1 1 2 3 5 8 13 21 34
