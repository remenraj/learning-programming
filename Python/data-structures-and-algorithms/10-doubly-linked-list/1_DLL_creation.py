# Doubly Linked List creation
# time complexity: O(1)
# space complexity: O(1)

class Node:
    """Node class for doubly linked list"""

    def __init__(self, value=None) -> None:
        """Initializes the node with value, next reference and prev references"""
        self.value = value  # value of current node
        self.next = None    # reference of the next node
        self.prev = None    # reference of the previous node


class DoublyLinkedList:
    def __init__(self) -> None:
        """Initiates head and tail to None"""
        self.head = None    # head
        self.tail = None    # tail
    
    
    def __iter__(self) -> None:
        """Iterate over the linked list to print the values"""
        node = self.head
        while node:
            yield node
            node = node.next
            
            
    def create_DLL(self, node_value) -> None:
        """Create a doubly linked list with a single node"""
        # creating a node
        node = Node(node_value)

        # assigning the previous and next node to null
        node.next = None
        node.prev = None
        
        # assigning the head and tail
        self.head = node
        self.tail = node
        

# creating an instance of doubly linked list
doubly_LL = DoublyLinkedList()

# creating a node with value = 1
doubly_LL.create_DLL(node_value=1)

print([node.value for node in doubly_LL])
