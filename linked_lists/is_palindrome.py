from linked_lists.node import Node


def revert_and_clone(head: Node) -> Node:
    new_head = None
    while head:
        node = Node(head.data)
        node.next = new_head
        new_head = node
        head = head.next
    return new_head


def is_palindrome(head: Node) -> bool:
    if not head:
        return True
    tail = revert_and_clone(head)
    while head and tail:
        if tail.data != head.data:
            return False
        tail = tail.next
        head = head.next

    return True
