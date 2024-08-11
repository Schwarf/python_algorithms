from linked_lists.node import Node


# O(N) time complexity, O(N) space complexity
def remove_duplicates(head: Node) -> Node:
    node_set = set()
    current = head
    previous = None
    while current:
        if current.data in node_set:
            previous.next = current.next
            current = previous.next
        else:
            node_set.add(current.data)
            previous = current
            current = current.next

    return head


# O(N^2) time complexity, O(1) space complexity
def remove_duplicates2(head: Node) -> Node:
    left = head
    while left:
        right = left.next
        previous = left
        while right:
            if right.data is left.data:
                previous.next = right.next
                right = previous.next
            else:
                previous = right
                right = right.next
        left = left.next
    return head


