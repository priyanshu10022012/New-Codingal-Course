# Program to find HCF/GCD
# Enter two numbers
numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))
#usimg Euclidean algorithm
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore
print(f"HCF of {numberLargest} and {numberSmallest} is: {numberLargest}")