def longest_consecutive(nums):
    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Test cases
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longest_consecutive([9, 1, 4, 7, 3, 2, 6, 5, 8, 10]))  # Output: 10
