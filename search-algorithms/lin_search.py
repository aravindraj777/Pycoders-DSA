def linear_search(arr,value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1





arr = [3,1,4,1,5,9,2,6,5,3,5]
value = 4
result = linear_search(arr,value)
print(result)

if(result != -1):
    print(f"value present in the index {result}")
else:
    print("Value not present in the list ")