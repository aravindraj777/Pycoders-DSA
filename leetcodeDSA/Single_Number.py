def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result


# Test cases
print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1]))
