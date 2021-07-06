'''
Say that you are a traveller on a 2D grid. You begin the top-left corner and your goal is to travel to bottom-right corner. You can only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n

Write a funtion "gridTraveler(m, n) that calculates this.
'''

def gridTraveler(m, n):
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

print(gridTraveler(1, 1))
print(gridTraveler(1, 0))
print(gridTraveler(5, 5))
print(gridTraveler(3, 4))
#print(gridTraveler(18,20)) This take way long time to execute. Time complexity => O(2**n)

# Alternative method using memoization
print("Using memoization method:")

def gridT(m, n, memo = dict()):
    
    key =  f"{m},{n}" #key = 3,4
    if key in memo:
        return memo[key]
    if m==0 or n==0:
        return 0
    if m==1 and n==1:
        return 1
    memo[key] = gridT(m-1,n,memo) + gridT(m, n-1, memo)
    return memo[key]

#print(gridT(1, 1))
#print(gridT(1, 0))
#print(gridT(5, 5))
print(gridT(3, 4))
#print(gridT(34, 43))

#Tabulation Method

def gridTravelert(m,n):
    table = [[0] * (n+1) for _ in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j+1 <= n:
                table[i][j+1] += current
            if i+1 <= m:
                table[i+1][j] += current
    return table[m][n]

print(gridTravelert(3,3))  
print(gridTravelert(34, 43))

'''
Time Complexity: O(mn)
Space Complexity: O(mn)
'''

