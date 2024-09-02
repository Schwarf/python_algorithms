from typing import List

import pytest

from dynamic_programming.coin_combinations import coin_combinations_classic, coin_combinations_top_down, \
    coin_combinations_bottom_up

test_cases = [
    ([1, 2, 5], 5, 4),
    ([5], 4, 0),
    ([1], 7, 1),
    ([1, 2, 5], 500, 12701)
]


@pytest.mark.parametrize("coins, amount, expected_result", test_cases)
def test_coin_combinations_classic(coins: List[int], amount: int, expected_result: int):
    assert coin_combinations_classic(coins, amount) == expected_result


###################################################################################
###################################################################################
###################################################################################

@pytest.mark.parametrize("coins, amount, expected_result", test_cases)
def test_coin_combinations_top_down(coins: List[int], amount: int, expected_result: int):
    assert coin_combinations_top_down(coins, amount) == expected_result


###################################################################################
###################################################################################
###################################################################################


@pytest.mark.parametrize("coins, amount, expected_result", test_cases)
def test_coin_combinations_bottom_up(coins: List[int], amount: int, expected_result: int):
    assert coin_combinations_bottom_up(coins, amount) == expected_result
