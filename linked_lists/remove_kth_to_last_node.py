from typing import Optional

from linked_lists.node import Node


# Given the head of a linked list, remove the nth node from the end of the list and return its head.


def remove_kth_to_last_node(head: Node, k: int) -> Node:
    # 'fast' and 'slow' pointers
    fast = slow = head

    # Move 'fast' pointer k steps ahead
    for _ in range(k):
        if fast is None:
            return head  # k is larger than the length of the list
        fast = fast.next

    # If 'fast' reaches the end, remove the head node
    if fast is None:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return head
