def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        elif arr[mid] > value:
            right = mid - 1
        else:
            return mid
    return -1




arr = [1,2,3,4,5]
value = 2
result = binary_search(arr, value)
print(result)

if(result != -1):
    print(f"value present in the index {result}")
else:
    print("Value not present in the list ")