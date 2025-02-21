def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid  # Peak is in the left half
        else:
            left = mid + 1  # Peak is in the right half

    return left  # or return right (both will be the peak index)

# Example Usage:
nums = [1,2,1,3,5,6,4]
print(find_peak_element(nums))  # Output: 5
