def howSum(targetSum, numbers):
    if(targetSum == 0):
        return []
    if(targetSum < 0):
        return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        if (remainderResult is not None):
            remainderResult.append(num)
            return remainderResult
        
    return None

print(howSum(7, [2,3]))
print(howSum(7, [5,3,4,7])) 
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))   

'''The above method doesnt work for larger array or if the targetSum is very large'''
'''m = targetSum, n = numbers length 
    Time Complexity: O(n^m * m)
    the extra m in TC is because of the appending
    Space complexity: O(m)'''

#Method 2 - Memoization

def howSum2(targetSum, numbers, memo = None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum2(remainder, numbers, memo)
        if remainderResult is not None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return memo[targetSum]

    memo[targetSum] = None
    return memo[targetSum]

print(howSum2(7, [2,3]))
print(howSum2(7, [5,3,4,7])) 
print(howSum2(7, [2,4]))
print(howSum2(8, [2,3,5]))
print(howSum2(300, [14,7,10,2])) 

"""Time complexity: O(n * m^2)
    Space complexity: O(m * m) = O(m^2)"""
