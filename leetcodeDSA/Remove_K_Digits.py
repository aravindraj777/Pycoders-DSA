def remove_k_digits(num, k):
    stack = []

    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # Remove remaining k digits from the end if needed
    stack = stack[:-k] if k > 0 else stack

    # Convert list to string and remove leading zeros
    result = "".join(stack).lstrip('0')

    return result if result else "0"

# Example Usage:
num = "1432219"
k = 3
print(remove_k_digits(num, k))  # Output: "1219"
