# Circular Singly Linked List Deletion

# deleting node
# time complexity: O(n)
# space complexity: O(1)

# deleting entire circular singly linked list
# time complexity: O(1)
# space complexity: O(1)

# Three cases:
# Deleting the first node: Linked list with one node, many nodes
# Deleting the last node: Linked list with one node, many nodes
# Deleting the given node


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
            node = node.next
            if node == self.tail.next:
                break
                        
    
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
    
    def insert_into_CSLL(self, value, location):
        """Inserts a node into the circular singly linked list"""
        # checking if there is no nodes in the linked list
        if self.head is None:
            return "the head reference is None"

        else:
            new_node = Node(value=value)
            
            # checking if the location is at the head
            if location == 0:
                new_node.next = self.head   # assigning the reference of first node to the new_node
                self.head = new_node    # assigning the new_node to the head
                self.tail.next = new_node  # assigning the reference of the new_node to the tail
            
            # checking if the location is at the tail
            elif location == 1:
                new_node.next = self.tail.next  # assigning the reference of the head to the new_node
                self.tail.next = new_node  # assigning the reference of the new_node to the last node
                self.tail = new_node  # assigning the new_node as the tail

            # inserting anywhere else
            else:
                # iterating over the linked list to find the location of the node to be inserted
                # new_node will be inserted between temp_node and temp_node.next
                temp_node = self.head
                index = 0
                while index < (location -1):
                    temp_node = temp_node.next
                    index += 1
                
                # new_node will be inserted between previous node and next node (temp_node and temp_node.next)
                # assigning the reference of the next node to the new node
                next_node = temp_node.next
                new_node.next = next_node
                # assinging the reference of the previous node to the new_node
                temp_node.next = new_node
                
                
    def delete_node(self, location) -> None:
        """Deletes a node from the circular singly linked list"""
        # checking for head, if head has reference, then there is a node present, else there is no node connected
        if self.head is None:
            print("The linked list is empty")
        
        # traverse through the list
        else:
            # checking if the location is at the head (deleting the first node)
            if location == 0:
                # checking if there is only one node in the linked list
                if self.head == self.tail:
                    self.head.next = None   # setting the first node's reference to None
                    self.head = None    # setting the head to None
                    self.tail = None    # setting the tail to None

                # more than one node in the linked list and deleting the first node
                else:
                    # assigning the reference of the next node(second node) to the head
                    self.head = self.head.next
                    # assigning the reference of the second node to the tail
                    self.tail.next = self.head
            
            # checking if the location is at the tail (deleting the last node)
            elif location == 1:
                # checking if there is only one node in the linked list
                if self.head == self.tail:
                    self.head.next = None   # setting the first node's reference to None
                    self.head = None    # setting the head to None
                    self.tail = None    # setting the tail to None

                # more than one node in the linked list and deleting the first node
                else:
                    # traverse the linked list to find the second last node
                    node = self.head
                    while node is not None:
                        # checking if the next node is the tail and breaking the loop if so
                        if node.next == self.tail:
                            break
                        # moving to the next node
                        node = node.next
                    
                    # assigning the reference of head to the second last node   
                    node.next = self.head
                    # assigning the second last node as tail
                    self.tail = node
            
            # deleting any other node
            else:
                temp_node = self.head  # temporary node to traverse the linked list
                index = 0

                # iterating over the linked list to find the node which is before the node we want to delete
                while index < (location - 1):
                    temp_node = temp_node.next
                    index += 1        
            

                # another simple way
                # before_node = temp_node  # assigning the reference of the node before the node we want to delete
                # to_delete_node = temp_node.next  # assigning the reference of the node we want to delete
                # after_node = to_delete_node.next
                # before_node.next = after_node  # assigning the reference of the node after the node we want to delete

                # next_node is the node to be deleted
                next_node = temp_node.next

                # connecting the previous node to the node after the node we want to delete
                # assigning the reference of the next node after the node we want to delete, to the previous node before the node we want to delete
                temp_node.next = next_node.next

    
    def delete_entire_CSLL(self) -> None:
        """"Deletes the entire circular singly linked list"""
        if self.head is None:
            print("The linked list is empty")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None
    
    
                
# creating an instance of circular singly linked list       
circular_SLL = CircularSinglyLinkedList()

# creating a node with value = 1
print(circular_SLL.create_CSLL(2))
print([node.value for node in circular_SLL])


# inserting values into the circular singly linked list
# inserting at the head
circular_SLL.insert_into_CSLL(value=1, location=0)
print([node.value for node in circular_SLL])

# inserting at the tail
circular_SLL.insert_into_CSLL(value=4, location=1)
print([node.value for node in circular_SLL])

# inserting at the 3rd location
circular_SLL.insert_into_CSLL(value=3, location=2)
print([node.value for node in circular_SLL])

# inserting at the last location
circular_SLL.insert_into_CSLL(value=5, location=1)
print([node.value for node in circular_SLL])

# inserting at the last location
circular_SLL.insert_into_CSLL(value=6, location=1)
print([node.value for node in circular_SLL])


# deleting the first node
circular_SLL.delete_node(location=0)
print([node.value for node in circular_SLL])

# deleting the last node
circular_SLL.delete_node(location=1)
print([node.value for node in circular_SLL])

# deleting the third node
circular_SLL.delete_node(location=2)
print([node.value for node in circular_SLL])

# deleting entire circular singly linked list
circular_SLL.delete_entire_CSLL()
print([node.value for node in circular_SLL])
