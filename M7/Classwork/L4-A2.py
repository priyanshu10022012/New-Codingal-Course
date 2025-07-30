n = int(input("Enter number of rows : "))
count = n-1

for i in range(0,n):
    for j in range(0,n):
        if j<count:
            print(" ", end="")
        else:
            print("*", end="")
    print("\n")
    count = count-1