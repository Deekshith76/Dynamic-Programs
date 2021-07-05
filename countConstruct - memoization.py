'''
Write a func countConstruct(target, wordBank) that accepts a target string and an array of strings

The func should return the no of ways that the target can be constructed by concatenating elements of wordBank array

You may reuse elements as much as you want
'''

#Brute Force
def countConstruct(target, wordBank):
    if target == "":
        return 1
    totalCount = 0
    for word in wordBank:
        if len(target) >= len(word) and target[: len(word)] == word:
            suffix = target[len(word): ]
            numWays = countConstruct(suffix, wordBank)
            totalCount = totalCount + numWays

    return totalCount

print(countConstruct('abcdef', ['ab','abc','cd','def','abcd']))
print(countConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
print(countConstruct('enterpotentpot', ['a','p','ent','enter','ot','o','t']))
print(countConstruct('purple', ['purp','p','ur','le','purpl']))

'''
Time Complexity: O(n^m * m)
Space Complexity: O(m^2)
'''

#Memoize

def countConstruct2(target, wordBank, memo = None):
    if memo is None:
        memo =  {}
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    totalCount = 0
    for word in wordBank:
        if len(target) >= len(word) and target[: len(word)] == word:
            suffix = target[len(word): ]
            numWays = countConstruct2(suffix, wordBank, memo) 
            totalCount += numWays
    memo[target] = totalCount
    return memo[target]

print(countConstruct('abcdef', ['ab','abc','cd','def','abcd']))
print(countConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
print(countConstruct('enterpotentpot', ['a','p','ent','enter','ot','o','t']))
print(countConstruct('purple', ['purp','p','ur','le','purpl']))
print(countConstruct2('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
      ['e',
       'ee',
       'eee',
       'eeee',
       'eeeee',
       'eeeeee',
       'f']))

'''
Time : O(n* m^2)
Space: O(m^2)
'''