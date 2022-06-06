# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference) as the
# jth node of the second linked list, then they are intersecting.

# 3 -> 6 -> 4 -> 5 -
#                    > 2 -> 6 -> 4 -> 5
#      4 -> 3 -> 2 -

# time_complexity = O(A + B)
# space_complexity = O(1)

from linked_list import LinkedList, Node


def intersection(ll_a: LinkedList, ll_b: LinkedList) -> Node:
    """
    Returns the intersection of two linked lists if any.
    """
    # check for intersection, if the tails are the same, then there is an intersection
    if ll_a.tail is not ll_b.tail:
        return None

    # compare the lengths of the lists to find the longest and shortest lists
    len_a = len(ll_a)
    len_b = len(ll_b)

    shorter = ll_a if len_a < len_b else ll_b
    longer = ll_b if len_a < len_b else ll_a
    # above condition works even if the lengths are equal

    # difference is calculated to iterate longer list ahead by difference, so as to get the distance to intersection is the same
    difference = len(longer) - len(shorter)

    # start of the list
    longer_node = longer.head
    shorter_node = shorter.head

    # iterate through the longer list until the difference is reached
    for _ in range(difference):
        longer_node = longer_node.next

    # iterate through the linked lists until the nodes are the same
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node
    return shorter_node


def add_same_node(ll_a: LinkedList, ll_b: LinkedList, value: int) -> LinkedList:
    """
    Adds intersection nodes to the linked list.
    """

    temp_node = Node(value)

    # Add the intersection node to the linked list and set it as the tail
    ll_a.tail.next = temp_node
    ll_a.tail = temp_node
    ll_b.tail.next = temp_node
    ll_b.tail = temp_node


if __name__ == "__main__":
    """Main function"""

    # generate linked lists
    ll_1 = LinkedList()
    ll_1.generate(n=3, min_value=1, max_value=10)

    ll_2 = LinkedList()
    ll_2.generate(n=4, min_value=1, max_value=10)

    add_same_node(ll_1, ll_2, value=3)
    add_same_node(ll_1, ll_2, value=6)
    add_same_node(ll_1, ll_2, value=4)

    print(ll_1)
    print(ll_2)

    print(intersection(ll_1, ll_2))
