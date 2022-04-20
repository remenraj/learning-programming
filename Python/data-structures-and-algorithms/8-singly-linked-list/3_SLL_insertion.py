# Insertion to linked list in memory
# time complexity: O(n)
# space complexity: O(1)

# Three cases:
# Insertion at the beginning of the linked list
# Insertion at the end of the linked list
# Insertion at the specific position of the linked list


class Node:
    """ Node of singly linked list"""
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        

class SinglyLinkedList:
    def __init__(self) -> None:
        """ Initialize head and tail to None"""
        self.head = None
        self.tail = None
    
    def __iter__(self) -> None:
        """ Iterate over the linked list to print the values"""
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert_into_SLL(self, value, location) -> None:
        """ Insertion of value into singly linked list"""
        new_node = Node(value)

        # checking if there is no nodes in the linked list
        if self.head is None:
            self.head = new_node    # assigning the reference of new_node to the head
            self.tail = new_node    # assigning new_node as the tail
        
        else:
            # checking if the location is at the head
            if location == 0:
                new_node.next = self.head   # assigning the reference of next node to the new_node (This is stored in head)
                self.head = new_node    # assigning the reference of the new_node to the head
            
            # checking if the location is at the tail
            elif location == 1:
                new_node.next = None    # at the end of the linked list, reference is Null/None
                self.tail.next = new_node   # assigning the reference of the new_node to the last node, previously it was the tail
                self.tail = new_node    # assigning new_node as the tail
            
            # inserting anywhere else
            else:
                # iterating over the linked list to find the location of the node to be inserted
                # new_node will be inserted between temp_node and temp_node.next
                temp_node = self.head
                index = 0
                while index < (location -1):
                    temp_node = temp_node.next
                    index += 1
                    
                # assigning the reference of the next node to the new node
                next_node = temp_node.next
                new_node.next = next_node
                
                # assigning the reference of the new node to the temp_node
                temp_node.next = new_node
                
                
singly_linked_list = SinglyLinkedList()

# Inserting values at the end of the singly linked list
singly_linked_list.insert_into_SLL(value=1, location=1)
singly_linked_list.insert_into_SLL(value=2, location=1)
singly_linked_list.insert_into_SLL(value=3, location=1)
singly_linked_list.insert_into_SLL(value=4, location=1)

print([node.value for node in singly_linked_list])


# inserting value at the beginning of the linked list
singly_linked_list.insert_into_SLL(value=0, location=0)
print([node.value for node in singly_linked_list])

# inserting value at the fourth location
singly_linked_list.insert_into_SLL(value=33, location=3)    # 33 is inserted after the 3rd element
print([node.value for node in singly_linked_list])


