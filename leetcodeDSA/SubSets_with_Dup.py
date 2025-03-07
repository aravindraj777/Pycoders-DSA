def subsetsWithDup(nums):
    res = []
    nums.sort()  # Sort to handle duplicates easily

    def backtrack(start, path):
        res.append(path[:])  # Append a copy of path

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            path.append(nums[i])  # Choose
            backtrack(i + 1, path)  # Explore
            path.pop()  # Unchoose (backtrack)

    backtrack(0, [])
    return res

# Example Usage:
nums = [1, 2, 2]
print(subsetsWithDup(nums))
# Output: [[], [1], [1,2], [1,2,2], [2], [2,2]]
