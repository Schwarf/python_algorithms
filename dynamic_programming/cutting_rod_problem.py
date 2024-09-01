# Given a rod of a certain length, and list of prices where a rod of length i provides the price
# prices[i] obtain the maximum total price for the rod. Cutting is free.
from typing import List


def cut_rod_recursive(length: int, prices: List[int]) -> int:
    if length <= 0:
        return 0
    total = 0
    for i in range(1, length+1):
        current_price = prices[i] if i < len(prices) else 0
        total = max(total, current_price + cut_rod_recursive(length-i, prices))
    return total


def memoization(length: int, prices: List[int], memo: List[int]) -> int:
    if length <= 0:
        return 0
    if memo[length] != -1:
        return memo[length]
    total = 0
    for i in range(1, length+1):
        current_price = prices[i] if i < len(prices) else 0
        total = max(total, current_price + cut_rod_recursive(length-i, prices))
        memo[length] = total
    return memo[length]


def cut_rod_top_down(length: int, prices: List[int]) -> int:
    memo = [-1]*(length+1)
    return memoization(length, prices, memo)


def cut_rod_bottom_up(length: int, prices: List[int]) -> int:
    dp = [0]*(length+1)
    for l in range(length+1):
        for i in range(l+1):
            current_price = prices[i] if i < len(prices) else 0
            dp[l] = max(dp[l], dp[l-i] + current_price)
    return dp[length]

