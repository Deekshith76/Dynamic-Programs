'''Write a function canConstruct(target, wordBank) that accepts a target string and array of strings

The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array

You may reuse elements of wordBank as many times as needed'''

# Brute Force 
def canConstruct(target, wordBank):
    if target == '':
        return True
    for word in wordBank:
        if len(target) >= len(word) and target[:len(word)] == word: 
            suffix = target[len(word):]  #slicing the word(prefix) from the target string 
            if(canConstruct(suffix, wordBank) == True):
                return True
            
    return False

print(canConstruct('abcdef', ['ab','abc','cd','def','abcd']))
print(canConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
print(canConstruct('enterpotentpot', ['a','p','ent','enter','et','o','t']))

'''
Time complexity: O(n^m * m)
Space complexity: O(m^2)
'''  

#Memoized

def canConstruct2(target, wordBank, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in wordBank:
        if len(target) >= len(word) and target[:len(word)] == word:
            suffix = target[len(word):]
            if(canConstruct2(suffix, wordBank, memo)):
                memo[target] = True
                return memo[target]
    memo[target] = False
    return memo[target]
        
print(canConstruct2('abcdef', ['ab','abc','cd','def','abcd']))
print(canConstruct2('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
print(canConstruct2('enterpotentpot', ['a','p','ent','enter','et','o','t']))
print(canConstruct2('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
      ['e',
       'ee',
       'eee',
       'eeee',
       'eeeee',
       'eeeeee', 
       'f']))

'''
m = target length
n = wordBank length
Time Complexity: O(n * m^2)
Space Complexity: O(m^2)
'''
         


