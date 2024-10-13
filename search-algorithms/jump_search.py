import math

def jump_search(arr, value):
    n = len(arr)
    jump = int(math.sqrt(n))
    low = 0
    
    for i in range(0, n, jump):
        if arr[i] == value:
            return i
        elif arr[i] < value:
            low = i
        else:
            break
    
    
    for i in range(low, min(low + jump , n)):
        if arr[i] == value:
            return i
    
    return -1       



arr = [1,2,3,4,5,6,7,8,9]
value = 4
index = jump_search(arr, value)

if index == -1:
    print("Not found")
else:
    print(f" value found at index {index}")