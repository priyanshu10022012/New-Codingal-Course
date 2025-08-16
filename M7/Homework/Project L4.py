# Armstrong Number Check Program

# Take input from the user
num = int(input("Enter a number: "))

# Convert number to string to easily get digits
digits = str(num)
power = len(digits)   # Number of digits

# Calculate sum of each digit raised to the power of number of digits
sum_of_powers = sum(int(digit) ** power for digit in digits)

# Check Armstrong condition
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")