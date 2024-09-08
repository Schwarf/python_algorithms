from typing import List

from linked_lists.split_linked_list_in_parts import split_linked_list_in_parts
from linked_lists.node import Node

import pytest

test_cases = [([1, 2, 3], 5, [[1], [2], [3], [], []]),
              ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
              ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
              ([1], 1, [[1]])]


def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result


@pytest.mark.parametrize("list_input, k, expected_result", test_cases)
def test_split_linked_list_in_parts(list_input: List[int], k: int, expected_result: List[List[int]]):
    linked_list = build_linked_list(list_input)
    result = split_linked_list_in_parts(linked_list, k)
    assert [linked_list_to_list(part) for part in result] == expected_result
