#Fibonacci Number =>  1, 1, 2, 3, 5, 8, 13, 21, ... F(n) = F(n-1) + F(n-2)

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(7)) #13
print(fib(2)) #1
# print(fib(50)) => it takes way long time to execute => time complexity: O(2**n) and space complexity: O(n) or height of tree

# Hence , the above method is not feasible.
'''
To solve this issue we need to use MEMOIZATION which keep track of my previous evaluated fib functions..
'''

def fibm(n, memo =dict()):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fibm(n-1, memo) + fibm(n-2, memo)
    return memo[n]

print(fibm(2))
print(fibm(7))
print(fibm(50)) 

'''Now its work. Here, the time complexity is O(n) and space complexity is O(n)
To make sure just draw the binary tree...
'''

#Tabulation

def fibt(n):
    table = [0] * (n+1) #one extra box than the input
    table[1] = 1
    for i in range(n-1):
        table[i+1] += table[i]
        table[i+2] += table[i]
    table[-1] += table[-2]
    return table[n]
    

print(fibt(6))
print(fibt(25))
print(fibt(2))
print(fibt(100))

"""
Time complexity: O(n)
Space complexity: O(n)
"""
    
    







        