from linked_lists.is_palindrome import is_palindrome
from tests.test_linked_list.helper_functions import build_linked_list, list_to_values


def test_is_palindrome_yes():
    # Create a linked list from a list of values
    values = [1, 2, 3, 3, 2, 1]
    head = build_linked_list(values)

    # Check the result
    assert is_palindrome(head) is True


def test_is_palindrome_yes2():
    # Create a linked list from a list of values
    values = [1, 2, 3, 2, 1]
    head = build_linked_list(values)

    # Check the result
    assert is_palindrome(head) is True


def test_is_palindrome_yes3():
    # Create a linked list from a list of values
    values = [1]
    head = build_linked_list(values)

    # Check the result
    assert is_palindrome(head) is True


def test_is_palindrome_yes4():
    # Create a linked list from a list of values
    values = []
    head = build_linked_list(values)

    # Check the result
    assert is_palindrome(head) is True


def test_is_palindrome_no():
    # Create a linked list from a list of values
    values = [1, 2, 3, 1]
    head = build_linked_list(values)

    # Check the result
    assert is_palindrome(head) is False


def test_is_palindrome_no2():
    # Create a linked list from a list of values
    values = [1, 2, 2, 2]
    head = build_linked_list(values)

    # Check the result
    assert is_palindrome(head) is False
