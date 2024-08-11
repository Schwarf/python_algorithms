from linked_lists.remove_duplicates import remove_duplicates
from tests.test_linked_list.helper_functions import build_linked_list, list_to_values


def test_remove_duplicate_in_last_node():
    # Create a linked list from a list of values
    values = [1, 2, 3, 4, 5, 5]
    head = build_linked_list(values)

    # Remove the 2nd to last node
    modified_head = remove_duplicates(head)

    # Check the result
    assert list_to_values(modified_head) == [1, 2, 3, 4, 5]


def test_remove_three_duplicates():
    # Create a linked list from a list of values
    values = [1, 2, 2, 3, 2, 4]
    head = build_linked_list(values)

    # Remove the 2nd to last node
    modified_head = remove_duplicates(head)

    # Check the result
    assert list_to_values(modified_head) == [1, 2, 3, 4]


def test_remove_all_but_head():
    # Create a linked list from a list of values
    values = [1, 1, 1, 1, 1, 1]
    head = build_linked_list(values)

    # Remove the 2nd to last node
    modified_head = remove_duplicates(head)

    # Check the result
    assert list_to_values(modified_head) == [1]
