'''Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments

The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum

If there is any tie for the shortest combination, you may return any one of the shortest'''

def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination != None:
            
            combination = remainderCombination + [num]
            
            if (shortestCombination ==  None or len(combination) < len(shortestCombination)):
                shortestCombination = combination
    
    return shortestCombination
            
print(bestSum(7, [2,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))

'''m = targetSum ; n = len(numbers)
    time complexity: O(n^m * m)
    space complexity: O(m*m) = O(m^2)'''

#Memoized solution

def bestSum2(targetSum, numbers, memo = None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum2(remainder, numbers, memo)
        
        if remainderCombination is not None:
            combination = remainderCombination + [num]
            
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination
    
    memo[targetSum] = shortestCombination
    return memo[targetSum]


print(bestSum2(7, [2,3,4,7]))
print(bestSum2(8, [2,3,5]))
print(bestSum2(8, [1,4,5]))
#print(bestSum2(100, [1,2,5,25]))

# Tabulation 

def bestSumt(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []
    
    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i+num <= targetSum:
                    combination = table[i] + [num]
                    if not(table[i+num]) or len(table[i+num]) > len(combination):
                        table[i+num] = combination
    return table[targetSum]

print(bestSumt(8, [2,3,5]))
print(bestSumt(8, [1,4,5]))
print(bestSumt(100, [25,1,2,4]))

'''
Time Complexity : O(m^2 * n)
Space Complexity: O(m^2)
'''