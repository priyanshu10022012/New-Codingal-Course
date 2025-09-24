def multiply_direct(n, m):
    return n * m


# Function 2: Using N iterations (repeated addition)
def multiply_iterative(n, m):
    result = 0
    for _ in range(abs(n)):   # repeat |n| times
        result += m
    # Handle negative N
    return result if n >= 0 else -result


# Main Program
if __name__ == "__main__":
    N = int(input("Enter value of N: "))
    M = int(input("Enter value of M: "))

    print("\nUsing 1 iteration (direct multiplication):")
    print(f"{N} × {M} = {multiply_direct(N, M)}")

    print("\nUsing N iterations (repeated addition):")
    print(f"{N} × {M} = {multiply_iterative(N, M)}")