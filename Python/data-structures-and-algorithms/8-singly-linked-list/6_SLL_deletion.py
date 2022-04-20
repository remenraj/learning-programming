# Singly Linked List Deletion

# deleting node
# time complexity: O(n)
# space complexity: O(1)

# deleting entire singly linked list
# time complexity: O(1)
# space complexity: O(1)

# Three cases:
# Deleting the first node: Linked list with one node, many nodes
# Deleting the last node: Linked list with one node, many nodes
# Deleting the given node

class Node:
    """Node of singly linked list"""

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        """Initialize head and tail to None"""
        self.head = None
        self.tail = None

    def __iter__(self) -> None:
        """Iterate over the linked list to print the values"""
        node = self.head
        while node:
            yield node
            node = node.next

    def insert_into_SLL(self, value, location) -> None:
        """Insertion into singly linked list"""
        new_node = Node(value=value)

        # checking if there is no nodes in the linked list
        if self.head is None:
            self.head = new_node  # assigning the reference of new_node to the head
            self.tail = new_node  # assigning new_node as the tail

        else:
            # checking if the location is at the head
            if location == 0:
                new_node.next = (
                    self.head
                )  # assigning the reference of next node to the new_node (This is stored in head)
                self.head = (
                    new_node  # assigning the reference of the new_node to the head
                )

            # checking if the location is at the tail
            elif location == 1:
                new_node.next = (
                    None  # at the end of the linked list, reference is Null/None
                )
                self.tail.next = new_node  # assigning the reference of the new_node to the last node, previously it was the tail
                self.tail = new_node  # assigning new_node as the tail

            # inserting anywhere else
            else:
                # iterating over the linked list to find the location of the node to be inserted
                # new_node will be inserted between temp_node and temp_node.next
                temp_node = self.head
                index = 0
                while index < (location - 1):
                    temp_node = temp_node.next
                    index += 1

                # assigning the reference of the next node to the new node
                next_node = temp_node.next
                new_node.next = next_node

                # assigning the reference of the new node to the temp_node
                temp_node.next = new_node

    def delete_node(self, location) -> None:
        """Deletion of node from singly linked list"""
        if self.head is None:
            print("Singly Linked List is empty")
        else:
            # checking if the location is at the head (deleting the first node)
            if location == 0:
                # checking if there is only one node in the linked list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                # more than one node in the linked list and deleting the first node
                else:
                    # assigning the reference of the next node(second node) to the head, which deletes the first node
                    self.head = self.head.next

            # checking if the location is at the tail (deleting the last node)
            elif location == 1:
                # checking if there is only one node in the linked list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                # more than one node in the linked list and deleting the last node
                else:
                    # traverse the linked list to find the second last node
                    node = self.head
                    while node is not None:
                        # checking if the next node is the tail and breaking the loop if so
                        if node.next == self.tail:
                            break
                        # moving to the next node
                        node = node.next
                    node.next = (
                        None  # assigning the reference of the second last node to None
                    )
                    self.tail = node  # assigning the second last node as the tail

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

    def delete_entire_SLL(self) -> None:
        """Deletion of entire singly linked list"""
        if self.head is None:
            print("Singly Linked List is empty")
        else:
            self.head = None
            self.tail = None


singly_linked_list = SinglyLinkedList()

# Inserting values at the end of the singly linked list
singly_linked_list.insert_into_SLL(value=1, location=1)
singly_linked_list.insert_into_SLL(value=2, location=1)
singly_linked_list.insert_into_SLL(value=3, location=1)
singly_linked_list.insert_into_SLL(value=4, location=1)
singly_linked_list.insert_into_SLL(value=5, location=1)
singly_linked_list.insert_into_SLL(value=6, location=1)
singly_linked_list.insert_into_SLL(value=7, location=1)


print([node.value for node in singly_linked_list])

# deleting the first node
singly_linked_list.delete_node(0)
print([node.value for node in singly_linked_list])

# deleting the last node
singly_linked_list.delete_node(1)
print([node.value for node in singly_linked_list])

# deleting the fourth node
singly_linked_list.delete_node(3)
print([node.value for node in singly_linked_list])


# deleting entire singly linked list
singly_linked_list.delete_entire_SLL()
print([node.value for node in singly_linked_list])
