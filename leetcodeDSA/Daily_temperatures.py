def daily_temperatures(temperatures):
    stack = []
    res = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            res[prev_index] = i - prev_index
        stack.append(i)

    return res

# Example Usage:
temperatures = [73,74,75,71,69,72,76,73]
print(daily_temperatures(temperatures))  # Output: [1,1,4,2,1,1,0,0]
