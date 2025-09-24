def OnTime(n):
    iteration = 0
    for i in range(1, n + 1):
        iteration += 1
    print("When n is",n,"Iterations =", iteration)
    
OnTime(10)
OnTime(20)
OnTime(30)
print("\n with increase in 'n' the time taken by the computer will increase")