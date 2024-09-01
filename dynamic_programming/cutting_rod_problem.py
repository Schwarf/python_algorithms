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

