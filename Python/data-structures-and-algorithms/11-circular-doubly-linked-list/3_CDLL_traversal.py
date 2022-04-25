# Circular Doubly Linked List traversal
# time complexity: O(n)
# space complexity: O(1)

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


    def traverse_CDLL(self) -> None:
        """Traverse the circular doubly linked list"""
        # checking if there is no nodes in the linked list
        if self.head is None:
            return "There is no nodes in the linked list"

        else:
            # starting from the head
            temp_node = self.head
            # iterating over the linked list to print the values
            while temp_node:
                print(temp_node.value)
                # breaking the loop if the next node is the tail
                if temp_node == self.tail:
                    break
                # moving to the next node
                temp_node = temp_node.next


    def reverse_traverse_CDLL(self) -> None:
        """Reverse traverse the circular doubly linked list"""
        # checking if there is no nodes in the linked list
        if self.head is None:
            return "There is no nodes in the linked list"

        else:
            # starting from the tail
            temp_node = self.tail
            # iterating over the linked list to print the values
            while temp_node:
                print(temp_node.value)
                # breaking the loop if the next node is the head
                if temp_node == self.head:
                    break
                # moving to the previous node
                temp_node = temp_node.prev


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
    print([node.value for node in circular_DLL])


    # traversing the circular doubly linked list
    circular_DLL.traverse_CDLL()

    # traversing the circular doubly linked list in reverse order
    circular_DLL.reverse_traverse_CDLL()
