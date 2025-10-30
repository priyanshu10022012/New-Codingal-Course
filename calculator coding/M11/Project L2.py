#Write a Program to check the rightmost set bit in your number
num = int(input("Enter a number: "))
 
if num == 0:
     print("No set bits")
else:
     position = 1
     while (num & 1) == 0:
            num = num >> 1
            position += 1
    
     print("Rightmost set bit is at position:", position)