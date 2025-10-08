'''
Find and print all numbers from  1 to 3000 that are both :
1. Prime numbers, and
2. Palindrome numbers(read the same backward and forward    )
'''
a = int(input("Enter your number : "))
for num in range(1, a + 1):
    c = 0
    rev = 0
    temp = num
    
    # checking prime
    for i in range(1, temp + 1):
        if temp % i == 0:
            c += 1
    if c == 2:
        # checking palindrome
        while temp > 0:

            rev = rev * 10 + (temp % 10)
            temp = temp // 10
        if rev == num:
            print(num)