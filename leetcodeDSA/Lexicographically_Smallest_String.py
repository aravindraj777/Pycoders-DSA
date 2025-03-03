def lexicographicallySmallestString(S, k):
    S = list(S)  # Convert string to list for mutability
    n = len(S)

    # If k == 1, we can only change the first k characters individually.
    for i in range(min(k, n)):
        if S[i] != 'a':
            S[i] = 'a'

    return "".join(S)

# Example Usage:
print(lexicographicallySmallestString("bca", 1))
print(lexicographicallySmallestString("zxy", 2))  # Output: "axx"
