# Creation of Circular Singly Linked List with single node
# time complexity: O(1)
# space complexity: O(1)

class Node:
    """Node of circular singly linked list"""

    def __init__(self, value=None) -> None:
        self.value = value  # value of current node
        self.next = None  # reference of the next node


class CircularSinglyLinkedList:
    def __init__(self) -> None:
        """Initiates head and tail to None"""
        self.head = None  # head
        self.tail = None  # tail

    def __iter__(self) -> None:
        """Iterate over the linked list to print the values"""
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
            
    
    def create_CSLL(self, node_value) -> str:
        """Create a circular singly linked list"""
        # creating a node
        node = Node(value=node_value)

        # referencing the node to itself
        node.next = node
        
        # assigning the head and tail
        self.head = node
        self.tail = node

        return "Created a circular singly linked list"
        
        
# creating an instance of circular singly linked list       
circular_SLL = CircularSinglyLinkedList()

# creating a node with value = 1
circular_SLL.create_CSLL(1)

print([node.value for node in circular_SLL])