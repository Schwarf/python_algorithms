from typing import List

from dynamic_programming.cutting_rod_problem import cut_rod_recursive, cut_rod_top_down, cut_rod_bottom_up
import pytest


test_cases = [
    (8, [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 22),
    (9, [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 25),
    (15, [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 43)
]


@pytest.mark.parametrize("length, prices, expected_result", test_cases)
def test_cut_rod_recursive(length: int, prices: List[int], expected_result: int):
    assert expected_result == cut_rod_recursive(length, prices)

#############################################################################################################
#############################################################################################################
#############################################################################################################


@pytest.mark.parametrize("length, prices, expected_result", test_cases)
def test_cut_rod_top_down(length: int, prices: List[int], expected_result: int):
    assert expected_result == cut_rod_top_down(length, prices)


#############################################################################################################
#############################################################################################################
#############################################################################################################

@pytest.mark.parametrize("length, prices, expected_result", test_cases)
def test_cut_rod_bottom_up(length: int, prices: List[int], expected_result: int):
    assert expected_result == cut_rod_bottom_up(length, prices)

