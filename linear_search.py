
def binary_search(array, target): 
    low  = 0
    high = len(array)-1

    while(low<=high):
        mid  = (low+high)//2 #floor division 
        if(array[mid]==target):
            return mid 
        elif(array[mid]<target):
            low = mid + 1
        elif(array[mid]>target):
            high = mid - 1
    else:
        return None
    
    
def recursive_binary_search(array, target):
    if len(array) == 0:
        return False
    else:
        midpoint = len(array)//2
        if array[midpoint] == target:
            return True
        else:
            if array[midpoint] < target:
                return recursive_binary_search(array[midpoint+1:], target)
            elif array[midpoint] > target:
                    return recursive_binary_search(array[:midpoint],target)

array  = []
for i in range(1, 101):
    array.append(i)

result = binary_search(array, -34)
if result != None:
    print("Target found at index: ",result)
else:
    print("Target do not exist in the list")
    
res = recursive_binary_search(array, 23)
if(res):
    print("Target found:", res)
else:
    print("Target do not belong to the list")


    

