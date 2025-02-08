def findDuplicate(numsArr):
    # Step 1: Detect cycle using slow and fast pointers
    slow = numsArr[0]
    fast = numsArr[0]

    while True:
        slow = numsArr[slow]  # Move one step
        fast = numsArr[numsArr[fast]]  # Move two steps
        if slow == fast:
            break  # Cycle detected

    # Step 2: Find the entrance of the cycle (duplicate number)
    slow = numsArr[0]  # Reset slow to the start
    while slow != fast:
        slow = numsArr[slow]
        fast = numsArr[fast]

    return slow  # The duplicate number


# Example Usage:
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # Output: 2
