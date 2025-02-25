def sum_subarray_mins(arr):
    MOD = 10**9 + 7
    stack = []
    res = 0
    prev_smaller = [0] * len(arr)
    next_smaller = [0] * len(arr)

    # Previous smaller element count
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        prev_smaller[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    stack.clear()

    # Next smaller element count
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        next_smaller[i] = stack[-1] - i if stack else len(arr) - i
        stack.append(i)

    # Calculate the sum
    for i in range(len(arr)):
        res = (res + arr[i] * prev_smaller[i] * next_smaller[i]) % MOD

    return res

# Example Usage:
arr = [3,1,2,4]
print(sum_subarray_mins(arr))  # Output: 17
