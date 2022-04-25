# Circular Doubly Linked List creation
# time complexity: O(1)
# space complexity: O(1)

class Node:
    """Node class for doubly linked list"""

    def __init__(self, value=None) -> None:
        self.value = value  # value of current node
        self.next = None    # reference of the next node
        self.prev = None    # reference of the previous node


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        """Initiates head and tail to None"""
        self.head = None
        self.tail = None
    
    
    def __iter__(self) -> None:
        """Iterate over the linked list to print the values"""
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    
    def create_CDLL(self, node_value) -> None:
        """Create a circular doubly linked list with a single node"""
        # creating a node
        new_node = Node(node_value)
        
        # referencing the node to itself
        new_node.next = new_node
        new_node.prev = new_node
        
        # assigning the head and tail
        self.head = new_node
        self.tail = new_node
        
        
if __name__ == "__main__":

    # creating an instance of circular singly linked list       
    circular_DLL = CircularDoublyLinkedList()

    # creating a node with value = 1
    circular_DLL.create_CDLL(node_value=1)

    print([node.value for node in circular_DLL])
