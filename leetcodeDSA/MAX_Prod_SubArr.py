def maxProduct(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]  # Tracks the smallest product (for negative numbers)
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product  # Swap when negative

        max_product = max(nums[i], nums[i] * max_product)
        min_product = min(nums[i], nums[i] * min_product)

        result = max(result, max_product)

    return result

# Example Usage:
nums = [2, 3, -2, 4]
print(maxProduct(nums))  # Output: 6
