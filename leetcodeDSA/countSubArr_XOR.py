def countSubarraysWithXOR(nums, K):
    xor_map = {0: 1}  # Stores prefix XOR frequencies
    prefix_xor = 0
    count = 0

    for num in nums:
        prefix_xor ^= num  # Compute the XOR up to the current index

        # Check if (prefix_xor ⊕ K) exists in the map
        required_xor = prefix_xor ^ K
        if required_xor in xor_map:
            count += xor_map[required_xor]

        # Store the current prefix_xor in the map
        xor_map[prefix_xor] = xor_map.get(prefix_xor, 0) + 1

    return count

# Example Usage:
nums = [4, 2, 2, 6, 4]
K = 6
print(countSubarraysWithXOR(nums, K))  # Output: 4

nums = [5, 6, 7, 8, 9]
K = 5
print(countSubarraysWithXOR(nums, K))  # Output: 2
