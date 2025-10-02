def myfunction1(n):
    if (n > 0):   # <- lagta hai is condition me galti hai (n>0 pe return kar raha hai, iska matlab loop kabhi chalega hi nahi)
        return
    for i in range(0, n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)
def myfunction2(n):
    if (n <= 1):
        return
    print("Codingal")
    myfunction2(n-1)
#recurrence relation of myfunction1 is T(n) = T(n/2) + T(n/3) + O(1)
#recurrence relation of myfunction2 is T(n) = T(n-1) + O(1)
#time complexity of myfunction1 is O(n^(log(5)/log(6)))
#time complexity of myfunction2 is O(n)