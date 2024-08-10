from typing import Optional

# Given the head of a linked list, remove the nth node from the end of the list and return its head.
class Node:
    def __init(self, data):
        self.data = data
        self.next = None


def remove_kth_to_last_node(head: Node, k: int) -> Optional[Node]:
    front = head
    back = head
    while front is not None and k > 0:
        front = front.next
        k -=1

    pre = None
    while front:
        front = front.next
        pre =back
        back = head.next

    pre.next = back.next

    return head



