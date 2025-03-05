def minOperationsToMakeXORZero(nums):
    total_xor = 0

    # Calculate the XOR of the entire array
    for num in nums:
        total_xor ^= num

    # If XOR is already 0, return 0 (no need to remove anything)
    if total_xor == 0:
        return 0

    # Check if any element in the array is equal to total_xor
    for num in nums:
        if num == total_xor:
            return 1  # Removing this element will make XOR zero

    # Otherwise, return -1 (impossible case)
    return -1

# Example Usage:
nums1 = [2, 3, 1, 6]
print(minOperationsToMakeXORZero(nums1))  # Output: 1

nums2 = [1, 2, 3]
print(minOperationsToMakeXORZero(nums2))  # Output: 0

nums3 = [5, 7, 9]
print(minOperationsToMakeXORZero(nums3))  # Output: -1
