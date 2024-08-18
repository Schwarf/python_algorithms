# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Can the last index be reached from the 0-index?
from typing import List


def can_reach_last_index(jump_distance: List) -> bool:
    n = len(jump_distance)
    if n - 1 == 0:
        return True
    if jump_distance[0] == n - 1:
        return True
    if jump_distance[0] == 0:
        return False
    current_position = n - 1
    for current_index in range(n - 1, -1, -1):
        if current_index + jump_distance[current_index] >= current_position:
            current_position = current_index

    return current_position == 0
