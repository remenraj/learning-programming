# Doubly Linked List search
# time complexity: O(n)
# space complexity: O(1)


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

    def search_DLL(self, node_value):
        """Search through the linked list to find the node with the given value"""
        # checking if there is no nodes in the linked list
        if self.head is None:
            return "The head reference is None"
        else:
            # starting from the first node
            temp_node = self.head
            
            # iterate over the linked list to find the value of the node to be searched
            while temp_node is not None:
                # checking for value
                if temp_node.value == node_value:
                    return temp_node.value
                
                temp_node = temp_node.next  # moving to the next node

            return "The value is not in the linked list"


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
print([node.value for node in doubly_LL])


# Searching for element in doubly linked list
print(doubly_LL.search_DLL(node_value=3))
print(doubly_LL.search_DLL(node_value=33))