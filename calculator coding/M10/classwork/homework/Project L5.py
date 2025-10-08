def find_gcd(a, b):
    """Function to find GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    """Function to calculate LCM"""
    return (a * b) // find_gcd(a, b)

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")