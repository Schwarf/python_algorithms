from linked_lists.node import Node


def build_linked_list(values):
    """ Helper function to build a linked list from a list of values. """
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


def list_to_values(head):
    """ Helper function to convert linked list back to a list of values for easy comparison. """
    values = []
    while head:
        values.append(head.data)
        head = head.next
    return values
