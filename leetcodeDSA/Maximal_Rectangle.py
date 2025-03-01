def maximal_rectangle(matrix):
    if not matrix:
        return 0

    def largest_histogram_area(heights):
        stack = []
        max_area = 0
        heights.append(0)  # Sentinel to flush out remaining stack elements

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # Restore original heights array
        return max_area

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == "1" else 0  # Update heights
        max_area = max(max_area, largest_histogram_area(heights))

    return max_area

# Example Usage:
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
print(maximal_rectangle(matrix))  # Output: 6
