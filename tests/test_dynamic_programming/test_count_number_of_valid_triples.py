from typing import List

import pytest

from dynamic_programming.count_number_of_valid_triples import valid_triples, valid_triples_dp

test_cases = [
    ([2, 5, 3, 4, 1], 3),
    ([2, 1, 3], 0),
    ([1, 2, 3, 4], 4),
    ([89, 61, 13, 36, 37, 39, 97, 76, 84, 18, 12, 24, 71, 33, 44, 85, 70, 82, 15, 74, 35, 66, 59,
      8, 3, 96, 30, 16, 41, 7, 10, 68, 92, 83, 95, 77, 9, 14, 81, 88, 38], 3514)
]


@pytest.mark.parametrize("input_array, expected_result", test_cases)
def test_valid_triples(input_array: List[int], expected_result: int):
    assert expected_result == valid_triples(input_array)


###################################################################################
###################################################################################
###################################################################################


@pytest.mark.parametrize("input_array, expected_result", test_cases)
def test_valid_triples_dp(input_array: List[int], expected_result: int):
    assert expected_result == valid_triples_dp(input_array)
