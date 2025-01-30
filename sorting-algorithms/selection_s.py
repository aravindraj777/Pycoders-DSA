def selection_sort(array):
    for i in range(0, len(array) - 1, 1):
        minimum = i
        for j in range(i + 1, len(array), 1):
            if arr[minimum] > arr[j]:
                minimum = j
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp
    return array


arr = [98, 23, 12, 14, 90, 20]
brr = selection_sort(arr)
print(brr)
