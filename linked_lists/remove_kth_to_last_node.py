from typing import Optional

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_kth_to_last_node(head: Node, k: int) -> Node:
    # 'front' and 'back' pointers
    front = back = head

    # Move 'front' pointer k steps ahead
    for _ in range(k):
        if front is None:
            return head  # k is larger than the length of the list
        front = front.next

    # If 'front' reaches the end, remove the head node
    if front is None:
        return head.next

    # Move both pointers until front reaches the end
    pre_back = back
    while front:
        front = front.next
        pre_back = back
        back = back.next


    pre_back.next = back.next

    return head

