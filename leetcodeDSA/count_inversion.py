def count_inversions(nums):
    def merge_sort(arr, temp_arr, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2
        inv_count = merge_sort(arr, temp_arr, left, mid)
        inv_count += merge_sort(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)

        return inv_count

    def merge(arr, temp_arr, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    return merge_sort(nums, [0] * len(nums), 0, len(nums) - 1)

# Example Usage
nums = [8, 4, 2, 1]
print(count_inversions(nums))  # Output: 6
