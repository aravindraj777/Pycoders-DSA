def subarraySum(numsArr, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}  # To handle the case where prefix_sum itself is k

    for num in numsArr:
        prefix_sum += num  # Update running sum

        # Check if (prefix_sum - k) exists in map
        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]

        # Store the prefix_sum frequency
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count


# Example Usage:
nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(subarraySum(nums, k))  # Output: 4
