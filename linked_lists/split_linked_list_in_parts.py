from typing import List

from node import Node


def split_linked_list_in_parts(head: Node, k: int) -> List[Node]:
    node = head
    n = 0
    while node:
        n += 1
        node = node.next
    additional_node = n % k
    nodes_per_list = int(n / k)
    result = [None] * k
    current = head
    for i in range(k):
        result[i] = current
        add = 1 if additional_node > 0 else 0
        previous = None
        for j in range(nodes_per_list + add):
            previous = current
            current = current.next
        if previous:
            previous.next = None

    return result
