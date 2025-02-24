def largest_rectangle_area(heights):
    stack = []
    max_area = 0

    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

# Example Usage:
heights = [2,1,5,6,2,3]
print(largest_rectangle_area(heights))  # Output: 10
