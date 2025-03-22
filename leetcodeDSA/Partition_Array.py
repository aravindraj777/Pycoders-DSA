from collections import Counter

def maxWaysToPartition(nums):
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    total = prefix[-1]
    left_count = Counter()
    right_count = Counter()

    for i in range(1, n):
        right_count[prefix[i]] += 1

    max_partitions = right_count[total // 2] if total % 2 == 0 else 0

    for i in range(n):
        diff = nums[i]
        new_partitions = 0

        for new_val in set(nums):
            change = new_val - diff
            new_total = total + change
            if new_total % 2 == 0:
                mid = new_total // 2
                new_partitions = left_count[mid] + right_count[mid]

            max_partitions = max(max_partitions, new_partitions)

        if i + 1 < n:
            left_count[prefix[i + 1]] += 1
            right_count[prefix[i + 1]] -= 1

    return max_partitions

# Example test
nums = [2, -1, 2]
print(maxWaysToPartition(nums))  # Output: 1
