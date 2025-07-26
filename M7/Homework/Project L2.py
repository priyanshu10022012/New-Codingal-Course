def swap_three_numbers():
# Read three integers from user input
a, b, c = map(int, input("Enter three numbers (a b c): ").split())

print(f"Before swapping: a = {a}, b = {b}, c = {c}")

# Swap cyclically: a ← c, b ← a, c ← b
a, b, c = c, a, b

print(f"After swapping: a = {a}, b = {b}, c = {c}")

if __name__ == "__main__":
swap_three_numbers()