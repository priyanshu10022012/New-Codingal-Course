# Program to find 2 digit prime numbers
# and check if they are palindrome
for num in range(10, 100):
    count = 0
    rev = 0
    temp = num

    # checking prime
    for i in range(1, temp + 1):
        if temp % i == 0:
            count += 1
    if count == 2:
        # checking palindrome
        while temp > 0:

            rev = rev * 10 + (temp % 10)
            temp = temp // 10
        if rev == num:
            print(num)