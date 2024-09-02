from dynamic_programming.count_unique_binary_search_trees import count_unique_bst_recursive, \
    count_count_unique_bst_bottom_up

import pytest

test_cases = [(1, 1), (3, 5), (10, 16796)]


@pytest.mark.parametrize("n, expected_result", test_cases)
def test_count_bst(n: int, expected_result: int):
    assert expected_result == count_unique_bst_recursive(n)

#############################################################
#############################################################
#############################################################


@pytest.mark.parametrize("n, expected_result", test_cases)
def test_count_bst_top_down(n: int, expected_result: int):
    assert expected_result == count_count_unique_bst_bottom_up(n)
