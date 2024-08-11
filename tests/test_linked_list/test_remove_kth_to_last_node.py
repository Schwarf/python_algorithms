from linked_lists.remove_kth_to_last_node import remove_kth_to_last_node
from tests.test_linked_list.helper_functions import build_linked_list, list_to_values


def test_remove_2nd_to_last_node():
    # Create a linked list from a list of values
    values = [1, 2, 3, 4, 5]
    head = build_linked_list(values)

    # Remove the 2nd to last node
    modified_head = remove_kth_to_last_node(head, 2)

    # Check the result
    assert list_to_values(modified_head) == [1, 2, 3, 5]

def test_remove_last_node():
    # Create a linked list from a list of values
    values = [1, 2, 3, 4, 5]
    head = build_linked_list(values)

    # Remove the 2nd to last node
    modified_head = remove_kth_to_last_node(head, 1)

    # Check the result
    assert list_to_values(modified_head) == [1, 2, 3, 4]


def test_remove_head_node():
    values = [1, 2, 3]
    head = build_linked_list(values)

    # Remove the head node (3rd to last)
    modified_head = remove_kth_to_last_node(head, 3)

    # Check the result
    assert list_to_values(modified_head) == [2, 3]


def test_remove_beyond_length():
    values = [1, 2]
    head = build_linked_list(values)

    # Attempt to remove a node beyond the length of the list
    modified_head = remove_kth_to_last_node(head, 5)

    # Expect no changes as the position is invalid
    assert list_to_values(modified_head) == [1, 2]

# Additional tests can be written to cover more scenarios
