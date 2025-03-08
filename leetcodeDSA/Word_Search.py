def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True  # Found the word

        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False  # Out of bounds or mismatch

        temp = board[r][c]
        board[r][c] = '#'  # Mark visited

        # Explore all four directions
        found = (backtrack(r + 1, c, index + 1) or
                 backtrack(r - 1, c, index + 1) or
                 backtrack(r, c + 1, index + 1) or
                 backtrack(r, c - 1, index + 1))

        board[r][c] = temp  # Unmark

        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and backtrack(r, c, 0):
                return True

    return False

# Example Usage:
board = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']]

word1 = "ABCCED"
print(exist(board, word1))  # Output: True

word2 = "SEE"
print(exist(board, word2))  # Output: True

word3 = "ABCB"
print(exist(board, word3))  # Output: False
