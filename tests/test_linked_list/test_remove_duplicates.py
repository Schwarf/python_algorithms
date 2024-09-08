from typing import List

from linked_lists.remove_duplicates import remove_duplicates, remove_duplicates2
from tests.test_linked_list.helper_functions import build_linked_list, list_to_values
import pytest

test_cases = [([1, 2, 3, 4, 5, 5], [1, 2, 3, 4, 5]),
              ([1, 2, 2, 3, 2, 4], [1, 2, 3, 4]),
              ( [1, 1, 1, 1, 1, 1], [1])]


@pytest.mark.parametrize("list_input, expected_result", test_cases)
def test_remove_duplicate(list_input: List[int], expected_result: List[int]):
    head = build_linked_list(list_input)
    modified_head = remove_duplicates(head)
    assert list_to_values(modified_head) == expected_result


@pytest.mark.parametrize("list_input, expected_result", test_cases)
def test_remove_duplicate2(list_input: List[int], expected_result: List[int]):
    head = build_linked_list(list_input)
    modified_head = remove_duplicates2(head)
    assert list_to_values(modified_head) == expected_result

