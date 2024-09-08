from typing import List

from linked_lists.is_palindrome import is_palindrome
from tests.test_linked_list.helper_functions import build_linked_list, list_to_values

import pytest

test_cases = [([1, 2, 3, 3, 2, 1], True),
              ([1, 2, 3, 2, 1], True),
              ([1], True),
              ([], True),
              ([1, 2, 3, 1], False),
              ([1, 2, 2, 2], False)]


@pytest.mark.parametrize("list_input, expected_result", test_cases)
def test_is_palindrome_yes(list_input: List[int], expected_result: bool):
    # Create a linked list from a list of values
    head = build_linked_list(list_input)
    assert is_palindrome(head) is expected_result
