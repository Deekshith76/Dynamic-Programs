'''
Write a funtion "canSum(targetSum, numbers)" that takes in a targetSum and an array of numbers as arguments.

The func should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.
You may assume that all input members are nonnegative
'''

def canSum(targetSum, numbers):
    if (targetSum == 0):
        return True
    if (targetSum < 0):
        return False
    for num in numbers:
        remainder = targetSum - num
        if(canSum(remainder, numbers)==True):
            return True
    return False    

#print(canSum(7, [2,3]))
#print(canSum(7, [5,3,4,7]))
#print(canSum(7, [2,4]))
#print(canSum(8, [2,3,5])) # => Time Complexity: O(n**m) => Space Complexity: O(m)

'''Memoizing it'''
'''memo will be initialised only once. So, if you are not passing memo while calling then the previous memo will be used which is not advisable in this case. In other words the value of default argument is evaluated only once, when the function is declared'''

'''A common way is to create a new mutable object by default everytime a function is called is to use an immutable placeholder value like None. The function looks for that placeholder value and when found, replaces it with a brand new instance of mutable type'''


def canSum2(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        remainder = targetSum - num
        if(canSum2(remainder, numbers, memo)==True):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False
    
print(canSum2(777, [2,4,6]))
print(canSum2(7, [2,3]))
print(canSum2(1, [5,3,4,7]))
print(canSum2(7, [2,4]))
print(canSum2(8, [2,3,5]))