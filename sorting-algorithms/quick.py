def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[n - 1]
    left = []
    right = []

    for i in range(n - 1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


new_arr = [2, 7, 5, 9, 6, 3, 8]
print(quick_sort(new_arr))