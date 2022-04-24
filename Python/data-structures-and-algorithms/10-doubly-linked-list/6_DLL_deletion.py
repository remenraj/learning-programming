# Doubly Linked List Deletion

# deleting node
# time complexity: O(n)
# space complexity: O(1)

# deleting entire doubly linked list
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


class DoublyLinkedList:
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

    def insert_into_DLL(self, value, location):
        """Inserts a node into the doubly linked list"""

        # checking if there is no nodes in the linked list
        if self.head is None:
            return "The head reference is None"

        else:
            new_node = Node(value=value)

            # checking if the location to insert is at the head
            if location == 0:
                # assigning the reference of previous and next node to new_node
                # new_node.prev = None    # already initialized to None
                new_node.next = self.head

                # assigning the reference of the previous node of head
                self.head.prev = new_node

                # assigning new_node as head
                self.head = new_node

            # checking if the location to insert is at the tail
            elif location == 1:
                # assigning the reference of previous and next node to new_node
                # new_node.next = None    # already initialized to None
                new_node.prev = self.tail

                # assigning the reference of new_node to the next reference of tail node (which is currently None)
                self.tail.next = new_node

                # assinging the new_node as tail
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

                # assigning the reference of previous and next node to new_node
                new_node.next = temp_node.next
                new_node.prev = temp_node

                # updating the previous reference of next node to new_node
                temp_node.next.prev = new_node

                # updating the next reference of previous node to new_node
                temp_node.next = new_node

    def delete_node(self, location):
        """Deletes a node from the doubly linked list"""
        # check if there is no nodes in the linked list
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            # checking if the location to delete is at the head
            if location == 0:
                # checking if there is only one node in the linked list
                # and setting head and tail to None if so
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    
                # more than one node in the linked list and deleting the first node
                else:
                    
                    # assigning the reference of second node to the head
                    self.head = self.head.next

                    # assigning the reference of the next node to None
                    self.head.prev = None
    
            # checking if the location to delete is at the tail
            elif location == 1:
                # checking if there is only one node in the linked list
                # and setting head and tail to None if so
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    
                # more than one node in the linked list and deleting the first node
                else:
                    # setting the reference of the second last node as tail
                    self.tail = self.tail.prev
                    
                    # setting the reference of the second last node as None
                    self.tail.next = None

            # deleting any other node
            else:
                temp_node = self.head  # temporary node to traverse the linked list
                index = 0

                # iterating over the linked list to find the node which is before the node we want to delete
                # location of the node to be deleted is the between temp_node(previous node) and temp_node.next.next(next node)
                while index < (location - 1):
                    temp_node = temp_node.next
                    index += 1

                # setting the previous reference of the next node to previous node
                temp_node.next.prev = temp_node
                
                # setting the next reference of the previous node to next node
                temp_node.next = temp_node.next.next
    
    
    def delete_entire_DLL(self):
        """Deletes the entire doubly linked list"""
        # check if there is no nodes in the linked list
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            # starting from the first node
            temp_node = self.head
            
            # iterating over the linked list to delete all the nodes
            while temp_node:
                temp_node.prev = None   # setting the previous reference of the current node to None
                temp_node = temp_node.next   # assigning the next reference of the current node to the next node
                
            # setting head and tail to None
            self.head = None
            self.tail = None
            print("The doubly linked list has been deleted")
                
# creating an instance of doubly linked list
doubly_LL = DoublyLinkedList()

# creating a node with value = 1
doubly_LL.create_DLL(node_value=2)
# inserting at the start
doubly_LL.insert_into_DLL(value=1, location=0)
# inserting at the end
doubly_LL.insert_into_DLL(value=4, location=1)
# inserting at the 3rd location
doubly_LL.insert_into_DLL(value=3, location=2)
# inserting 5 at the end
doubly_LL.insert_into_DLL(value=5, location=1)
# inserting 6 at the end
doubly_LL.insert_into_DLL(value=6, location=1)
print([node.value for node in doubly_LL])


# deleting the first node
doubly_LL.delete_node(location=0)
print([node.value for node in doubly_LL])

# deleting the last node
doubly_LL.delete_node(location=1)
print([node.value for node in doubly_LL])

# deleting the third node
doubly_LL.delete_node(location=2)
print([node.value for node in doubly_LL])

# deleting the second node
# if we call delete_node with any negative value, it'll delete the second node
doubly_LL.delete_node(location=-11)
print([node.value for node in doubly_LL])

doubly_LL.delete_entire_DLL()
print([node.value for node in doubly_LL])
