# Traversal of Circular Singly Linked List
# time complexity: O(n)
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
                
    
    def traverse_CSLL(self):
        """Traverse the circular singly linked list"""
        # checking for head, if head has reference, then there is a node present, else there is no node connected
        if self.head is None:
            return "The head reference is None"
        
        # traverse through the list
        else:
            # starting from the first node
            node = self.head
            
            while node:
                print(node.value)   # printing the value of the node
                node = node.next    # assigning the reference of the next node to the node

                # breaking the loop if the node is the head
                if node == self.head:
                    break
                
                
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


circular_SLL.traverse_CSLL()