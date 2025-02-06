def findTheDifference(s: str, t: str) -> str:
    char_sum_s = sum(ord(c) for c in s)
    char_sum_t = sum(ord(c) for c in t)
    return chr(char_sum_t - char_sum_s)


print(findTheDifference("abcd", "abcde"))
print(findTheDifference("", "y"))
