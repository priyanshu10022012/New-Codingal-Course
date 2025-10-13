def myfunction(n):
    for i in range(0,n+1):          # Loop 1
        print("First loop")
    
    j=1
    while(j<=n+1):                  # Loop 2
        print("Second loop",j)
        j=j*2
    
    for i in range(0,100):          # Loop 3
        print("Third loop")
# Total Time Complexity analysis:
# Loop 1 runs (n+1) times => O(n)
# Loop 2 runs log(n) times => O(log n)
# Loop 3 runs 100 times => O(1)
# Overall Time Complexity: O(n) + O(log n) + O(1) = O(n)
# Overall Time Complexity: O(n)