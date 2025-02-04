def first_unique_char(s: str) -> int:
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1


# Test Cases
print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
