def canJump(nums):
    maxReach = 0  # Tracks the farthest index we can reach
    for i, jump in enumerate(nums):
        if i > maxReach:  # If we reach a point that is not accessible
            return False
        maxReach = max(maxReach, i + jump)  # Update the farthest reachable index
    return True


print(canJump([2,3,1,1,4]))  # Output: True
print(canJump([3,2,1,0,4]))  # Output: False
