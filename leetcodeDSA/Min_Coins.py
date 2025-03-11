def minCoins(coins, amount):
    coins.sort(reverseg=True)  # Sort coins in descending order
    count = 0  # To count the number of coins
    for coin in coins:
        if amount >= coin:
            count += amount // coin  # Use as many of this coin as possible
            amount %= coin  # Reduce the remaining amount
    return count if amount == 0 else -1  # Return -1 if amount can't be formed


print(minCoins([1, 2, 5], 11))  # Output: 3 (5+5+1)
print(minCoins([2], 3))  # Output: -1
print(minCoins([9, 6, 1], 11))  # Output: 2 (9+1+1)
