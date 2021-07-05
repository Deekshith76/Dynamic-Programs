"""
Write a function allConstruct(target, wordBank) that accepts a target string and an array of strings.

The function should return a 2D array containing all of the ways that the target can be constructed by concatenating elements of the wordBank array. Each element of the 2D array should represent one combination that construct the target
"""

def allConstruct(target, wordBank):
    if target == "":
        return [[]]
    result = []
    for word in wordBank:
        if len(target) >= len(word) and target[: len(word)] == word:
            suffix = target[len(word): ]
            suffixWays = allConstruct(suffix, wordBank)
            targetWays = [ [word] + way for way in suffixWays]
            if targetWays:
                result.extend(targetWays)
    return result

print(allConstruct('purple', ['purp','p','ur','le','purpl']))
print(allConstruct('abcdef', ['ab','abc','cd','def','abcd','ef','c']))
print(allConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))

#memoize

def allConstruct2(target, wordBank, memo=None):
    if memo is None:
        memo =  {}
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    result = []
    for word in wordBank:
        if len(target) >= len(word) and target[: len(word)] == word:
            suffix = target[len(word):]
            suffixWays = allConstruct2(suffix, wordBank, memo)
            targetWays = [[word] + way for way in suffixWays]
            if targetWays:
                result.extend(targetWays)
    memo[target] = result
    return memo[target]

print(allConstruct2('purple', ['purp','p','ur','le','purpl']))
print(allConstruct2('abcdef', ['ab','abc','cd','def','abcd','ef','c']))
print(allConstruct2('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
print(allConstruct2('aaaaaaaaaaaaaaaaaaaaaaaaz',['a','aa','aaa','aaaa','aaaaa','aaaaaaa']))

'''
Brute Force and Memoize:
Time - O(n^m)
Space - O(m)
'''