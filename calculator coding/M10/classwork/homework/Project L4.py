# Project: Understanding Binary and Decimal Conversions in Computers

# Function to convert decimal to binary
def decimal_to_binary(n):
    return bin(n).replace("0b", "")   # removes the '0b' prefix

# Function to convert binary to decimal
def binary_to_decimal(bstr):
    return int(bstr, 2)   # base 2 conversion

# Binary addition
def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2)).replace("0b", "")

# Binary multiplication
def binary_multiply(a, b):
    return bin(int(a, 2) * int(b, 2)).replace("0b", "")

# ------------------ Demonstration ------------------
print("=== Decimal ↔ Binary Conversion ===")
num = 13
print(f"Decimal {num} → Binary:", decimal_to_binary(num))

binary_num = "1101"
print(f"Binary {binary_num} → Decimal:", binary_to_decimal(binary_num))

print("\n=== Binary Arithmetic ===")
a = "1010"  # 10 in decimal
b = "0011"  # 3 in decimal
print(f"{a} + {b} = {binary_add(a, b)} (Binary)")
print(f"{a} × {b} = {binary_multiply(a, b)} (Binary)")
