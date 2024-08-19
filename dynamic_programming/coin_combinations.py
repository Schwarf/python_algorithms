from typing import List


# You are given an integer array coins representing coins of different denominations and an integer amount
# representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.

def coin_combinations_classic(coins: List[int], amount: int, index: int = 0) -> int:
    if amount is 0:
        return 1
    if amount < 0 or index >= len(coins):
        return 0

    with_current_coin = coin_combinations_classic(coins, amount - coins[index], index)
    without_current_coin = coin_combinations_classic(coins, amount, index + 1)
    return without_current_coin + with_current_coin


def coin_combinations_top_down(coins: List[int], amount: int) -> int:
    memo = [[-1] * (amount + 1) for _ in range(len(coins))]
    return top_down_implementation(coins, amount, memo, 0)


def top_down_implementation(coins: List[int], amount: int, memo: List[List[int]], index: int) -> int:
    if amount is 0:
        return 1
    if amount < 0 or index >= len(coins):
        return 0

    if memo[index][amount] != -1:
        return memo[index][amount]

    with_current_coin = top_down_implementation(coins, amount - coins[index], memo, index)
    without_current_coin = top_down_implementation(coins, amount, memo, index + 1)
    memo[index][amount] = without_current_coin + with_current_coin
    return memo[index][amount]


def coin_combinations_bottom_up(coins: List[int], amount: int) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]
