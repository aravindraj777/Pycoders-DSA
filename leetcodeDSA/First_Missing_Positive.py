def firstMissingPositive(numsArr):
    n = len(numsArr)

    # Step 1: Place numbers in their correct index (Cyclic Sort approach)
    for i in range(n):
        while 1 <= numsArr[i] <= n and numsArr[numsArr[i] - 1] != numsArr[i]:
            numsArr[numsArr[i] - 1], numsArr[i] = numsArr[i], numsArr[numsArr[i] - 1]  # Swap

    # Step 2: Find the first missing positive
    for i in range(n):
        if numsArr[i] != i + 1:
            return i + 1

    return n + 1  # If all numbers are in place, return n+1


# Example Usage:
nums = [3, 4, -1, 1]
print(firstMissingPositive(nums))  # Output: 2
