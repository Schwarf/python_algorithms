from linked_lists.node import Node


def remove_duplicates(head: Node) -> Node:
    node_set = set()
    current = head
    prev = None
    while current:
        if current.data in node_set:
            prev.next = current.next
            current = prev.next
        else:
            node_set.add(current.data)
            prev = current
            current = current.next

    return head



