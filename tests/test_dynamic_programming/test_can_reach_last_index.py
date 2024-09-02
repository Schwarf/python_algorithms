from typing import List

import pytest

from dynamic_programming.can_reach_last_index import can_reach_last_index

test_cases = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([0, 3, 1, 1, 4], False),
    ([4, 0, 0, 0, 0], True),
    ([0], True)
]


@pytest.mark.parametrize("jump_distances, can_reach_end", test_cases)
def test_can_reach_last_index(jump_distances: List[int], can_reach_end: bool):
    assert can_reach_last_index(jump_distances) is can_reach_end
