# Creation of singly linked list

# Create Head and Tail, initialize with null.
# Create a blank Node and assign a value to it and reference to null.
# Link Head and Tail with these Node.

# time complexity: O(1)
# space complexity: O(1)


class Node:
    """Node of singly linked list"""

    def __init__(self, data=None) -> None:
        self.data = data  # value of current node
        self.next = None  # reference of the next node


class SinglyLinkedList:
    def __init__(self) -> None:
        """Initiates head and tail to None"""
        self.head = None  # head
        self.tail = None  # tail

    def __iter__(self) -> None:
        """Iterate over the linked list to print the values"""
        node = self.head
        while node:
            yield node
            node = node.next


# create a node and assign a value to it and reference to null.
singly_linked_list = SinglyLinkedList()

# creating a node and assigning a value to it and reference to null.
node1 = Node(data=1)
node2 = Node(data=2)

# link head and tail with these node.
singly_linked_list.head = node1  # reference of the node1 is assigned to head
singly_linked_list.head.next = node2  # node1.next = node2, connects the next node
singly_linked_list.tail = node2 # assigning the tail to node2

# printing the data
print([node.data for node in singly_linked_list])

