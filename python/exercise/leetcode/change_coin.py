"""
You are given an integer array coins representing coins of different denominations and 
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount
of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
-----------
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""


# this is a comment.
def solution(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    change = 0
    coins = sorted(coins, reverse=True)
    print("coins", coins)
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change += 1
            print("Amount:", amount, "Change:", change, "Coin", coin)

    if change == 0:
        return -1
    print(amount)
    return change


print(solution([186, 419, 83, 408], 6249))
# assert solution([1, 2, 5], 11) == 3
