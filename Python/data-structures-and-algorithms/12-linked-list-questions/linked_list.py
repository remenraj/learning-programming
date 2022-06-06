# Generalized linked list

from random import randint


class Node:
    """Node class for a linked list"""

    def __init__(self, value) -> None:
        """Initialize a node with a value and references to null"""
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        """Return a string representation of the node, used for printing the value of the node"""
        return str(self.value)


class LinkedList:
    """Linked list class"""

    def __init__(self, values=None) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) -> None:
        """Return an iterator for the linked list, used for iterating over the linked list"""
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __str__(self) -> str:
        """Return a string representation of the linked list, used for printing the linked list"""
        # values = []
        # for node in self:
        #     values.append(str(node.value))

        values = [str(node.value) for node in self]

        return " -> ".join(values)

    def __len__(self) -> int:
        """Return the length of the linked list"""
        length = 0
        # for node in self:
        #     length += 1
        # return length
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def add(self, value) -> None:
        """Add a node with the given value to the linked list"""
        new_node = Node(value)
        # check if the linked list is empty and add a node to it if so
        if self.head is None:
            # assign head and tail to the new node
            self.head = new_node
            self.tail = new_node

        # else add the node to the end of the linked list
        else:
            self.tail.next = new_node  # set the next node of the tail to the new node
            new_node.prev = (
                self.tail
            )  # set the previous node of the new node to the tail
            self.tail = new_node  # set the tail to the new node

    def generate(self, n: int, min_value: int, max_value: int) -> None:
        """Generate a linked list of n nodes with random values between min_value and max_value"""

        # setting the head and tail to null
        self.head = None
        self.tail = None
        # adding n nodes to the linked list
        for _ in range(n):
            self.add(randint(min_value, max_value))


if __name__ == "__main__":
    # creating an instance of the linked list
    custom_LL = LinkedList()

    # creating a random linked list
    custom_LL.generate(n=10, min_value=0, max_value=99)

    # printing the linked list
    print(custom_LL)

    # printing the length of linked list
    print(len(custom_LL))
