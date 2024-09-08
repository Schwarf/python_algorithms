from linked_lists.remove_kth_to_last_node import remove_kth_to_last_node
from tests.test_linked_list.helper_functions import build_linked_list, list_to_values
import pytest

test_cases = [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
              ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
              ([1, 2, 3], 3, [2, 3]),
              ([1, 2], 5, [1, 2])]


@pytest.mark.parametrize("list_input, k, expected_result", test_cases)
def test_remove_2nd_to_last_node(list_input, k, expected_result):
    head = build_linked_list(list_input)
    modified_head = remove_kth_to_last_node(head, k)
    assert list_to_values(modified_head) == expected_result
