def validate_stack_sequences(pushed, popped):
    stack = []
    i = 0  # Pointer for popped array

    for num in pushed:
        stack.append(num)  # Push element into stack
        while stack and stack[-1] == popped[i]:  # Check if top of stack matches popped order
            stack.pop()
            i += 1

    return not stack  # If stack is empty, sequence is valid

# Example Usage:
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validate_stack_sequences(pushed, popped))  # Output: True
