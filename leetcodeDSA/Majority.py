def majorityElement(nums):
    candidate, count = None, 0

    # Phase 1: Find the candidate
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Phase 2: Verify if the candidate is actually a majority
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return -1  # No majority element found

# Example Usage:
nums = [3, 3, 4, 2, 3, 3, 3]
print(majorityElement(nums))  # Output: 3

nums = [1, 2, 3, 4]
print(majorityElement(nums))  # Output: -1
