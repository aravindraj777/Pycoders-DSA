def countNiceSubarrays(nums, k):
    def atMostK(nums, k):
        left = count = 0
        odd_count = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:  # Check if it's an odd number
                k -= 1

            while k < 0:  # If we exceed k odd numbers, shrink the window
                if nums[left] % 2 == 1:
                    k += 1
                left += 1

            count += (right - left + 1)  # Count subarrays ending at `right`

        return count

    return atMostK(nums, k) - atMostK(nums, k - 1)


nums1 = [1, 1, 2, 1, 1]
k1 = 3
print(countNiceSubarrays(nums1, k1))  # Output: 2

nums2 = [2, 4, 6]
k2 = 1
print(countNiceSubarrays(nums2, k2))  # Output: 0

nums3 = [1, 1, 1, 1, 1]
k3 = 2
print(countNiceSubarrays(nums3, k3))  # Output: 6
