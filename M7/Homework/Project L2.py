def swap_three_numbers():
    # Prompt user until valid input is given
    while True:
        try:
            a, b, c = map(int, input("Enter three integers separated by spaces: ").split())
            break
        except ValueError:
            print("Invalid input. Please enter exactly three integers, e.g. 10 20 30.")

    print(f"\nBefore swapping:\n  a = {a}\n  b = {b}\n  c = {c}")

    # Perform cyclic swap: a ← c, b ← a, c ← b
    a, b, c = c, a, b

    print(f"\nAfter swapping:\n  a = {a}\n  b = {b}\n  c = {c}")

if __name__ == "__main__":
    swap_three_numbers()
