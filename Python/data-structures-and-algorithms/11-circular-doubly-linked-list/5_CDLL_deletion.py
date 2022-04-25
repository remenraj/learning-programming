# Circular Doubly Linked List Deletion

# deleting node
# time complexity: O(n)
# space complexity: O(1)

# deleting entire circular doubly linked list
# time complexity: O(n)
# space complexity: O(1)

# Three cases:
# Deleting the first node: Linked list with one node, many nodes
# Deleting the last node: Linked list with one node, many nodes
# Deleting the given node

class Node:
    """Node class for doubly linked list"""

    def __init__(self, value=None) -> None:
        self.value = value  # value of current node
        self.next = None  # reference of the next node
        self.prev = None  # reference of the previous node


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

    def insert_into_CDLL(self, value, location):
        """Insert a node into the circular doubly linked list"""
        # checking if there is no nodes in the linked list
        if self.head is None:
            return "There is no nodes in the linked list"

        else:
            # creating a new node
            new_node = Node(value)

            # checking if the location to insert is at the head
            if location == 0:
                # assigning the next and prev references of new_node
                new_node.prev = self.tail  # reference of last node to the new_node
                new_node.next = self.head  # reference of first node to the new_node

                # assigning reference of new_node to prev reference of first node
                self.head.prev = new_node

                # assigning the reference of new_node to the next reference of last node
                self.tail.next = new_node

                # updating the head, setting the new_node as the head
                self.head = new_node

            # checking if the location to insert is at the tail
            elif location == 1:
                # assigning the next and prev references of new_node
                new_node.prev = self.tail
                new_node.next = self.head

                # assigning the reference of new_node to the next reference of last node
                self.tail.next = new_node

                # assigning the reference of new_node to the prev reference of first node
                self.head.prev = new_node

                # updating the tail, setting new_node as the new tail
                self.tail = new_node

            # inserting the new node anywhere else
            else:
                # iterating over the linked list to find the location of the node to be inserted
                # new_node will be inserted between temp_node and temp_node.next
                temp_node = self.head
                index = 0
                while index < (location - 1):
                    temp_node = temp_node.next
                    index += 1

                # assigning the prev and next references of new_node
                new_node.prev = temp_node
                new_node.next = temp_node.next

                # updating the prev reference of next node(temp_node.next)
                temp_node.next.prev = new_node

                # updating the next reference of temp_node
                temp_node.next = new_node

    def delete_node(self, location):
        """Delete a node from the circular doubly linked list"""
        # checking if there is no nodes in the linked list
        if self.head is None:
            return "There is no nodes in the linked list"

        else:
            # checking if the location to delete is at the head
            if location == 0:
                # checking if there is only one node in the linked list
                if self.head == self.tail:
                    # updating the prev and next reference of the node to be deleted
                    self.head.next = None   
                    self.head.prev = None  
                    # updating the head and tail 
                    self.head = None    # setting the head to None
                    self.tail = None    # setting the tail to None

                # more than one node in the linked list and deleting the first node
                else:
                    # updating the head
                    self.head = self.head.next

                    # updating the prev reference of first node
                    self.head.prev = self.tail

                    # updating the next reference of last node
                    self.tail.next = self.head

            # checking if the location to delete is at the tail
            elif location == 1:
                # checking if there is only one node in the linked list
                if self.head == self.tail:
                    # updating the prev and next reference of the node to be deleted
                    self.head.next = None   
                    self.head.prev = None  
                    # updating the head and tail 
                    self.head = None    # setting the head to None
                    self.tail = None    # setting the tail to None
                    
                # more than one node in the linked list and deleting the first node
                else:
                    # updating the tail
                    self.tail = self.tail.prev

                    # updating the next reference of last node
                    self.tail.next = self.head

                    # updating the prev reference of first node
                    self.head.prev = self.tail

            # deleting the node anywhere else
            else:
                # iterating over the linked list to find the location of the node to be deleted
                # location of the node to be deleted is between temp_node(previous node) and temp_node.next.next(next node)
                temp_node = self.head
                index = 0
                while index < (location - 1):
                    temp_node = temp_node.next
                    index += 1

                # assigning the reference of next node to the next reference of previous node
                temp_node.next = temp_node.next.next
                
                # assigning the reference of previous node to the prev reference of next node
                temp_node.next.prev = temp_node

    
    def delete_entire_CDLL(self) -> None:
        """Delete the entire circular doubly linked list"""
        # checking if there is no nodes in the linked list
        if self.head is None:
            return "There is no nodes in the linked list"

        else:
            # setting last node's next reference to null
            self.tail.next = None
            
            # iterating over the linked list to delete all the nodes
            temp_node = self.head
            while temp_node:
                temp_node.prev = None   # setting the previous reference of the current node to None
                temp_node = temp_node.next   # assigning the next reference of the current node to the next node
            
            # updating the head and tail 
            self.head = None    # setting the head to None
            self.tail = None    # setting the tail to None

            print("The circular linked list has been deleted")


if __name__ == "__main__":

    # creating an instance of circular singly linked list
    circular_DLL = CircularDoublyLinkedList()

    # creating a node with value = 2
    circular_DLL.create_CDLL(node_value=2)
    # inserting at the start
    circular_DLL.insert_into_CDLL(value=1, location=0)
    # inserting at the end
    circular_DLL.insert_into_CDLL(value=4, location=1)
    # inserting at the end
    circular_DLL.insert_into_CDLL(value=5, location=1)
    # inserting at the third location
    circular_DLL.insert_into_CDLL(value=3, location=2)
    # inserting at the end
    circular_DLL.insert_into_CDLL(value=6, location=1)
    print([node.value for node in circular_DLL])


    # deleting the first node
    circular_DLL.delete_node(location=0)
    print([node.value for node in circular_DLL])

    # deleting the last node
    circular_DLL.delete_node(location=1)
    print([node.value for node in circular_DLL])

    # deleting the third node
    circular_DLL.delete_node(location=2)
    print([node.value for node in circular_DLL])

    # deleting the second node
    circular_DLL.delete_node(location=-1)
    print([node.value for node in circular_DLL])

    # deleting the entire CDLL
    circular_DLL.delete_entire_CDLL()
    print([node.value for node in circular_DLL])