# Singly Linked List Search
# time complexity: O(n)
# space complexity: O(1)


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

    def search_SLL(self, node_value):

        # checking for head, if head has reference, then there is a node present, else there is no node connected
        if self.head is None:
            return "Single Linked List does not exist."
        else:
            # starting from the first node
            node = self.head
            while node is not None:
                # checking for value
                if node.value == node_value:
                    return node.value
                node = node.next  # assigning the next node
            return "The value does not exist in this list"


singly_linked_list = SinglyLinkedList()

# searching when there is node connected
print(singly_linked_list.search_SLL(3))


# Inserting values at the end of the singly linked list
singly_linked_list.insert_into_SLL(value=1, location=1)
singly_linked_list.insert_into_SLL(value=2, location=1)
singly_linked_list.insert_into_SLL(value=3, location=1)
singly_linked_list.insert_into_SLL(value=4, location=1)

print([node.value for node in singly_linked_list])


# Searching for element in Singly Linked List
print(singly_linked_list.search_SLL(3))
print(singly_linked_list.search_SLL(33))
