# Remove duplicates from an unsorted linked list
# With buffer:
# time complexity: O(n)
# space complexity: O(n)

# Without buffer:
# time complexity: O(n^2)
# space complexity: O(1)

from linked_list import LinkedList


def remove_duplicates(linked_list: LinkedList) -> LinkedList:
    """Remove duplicates from an unsorted linked list using temporary buffer and returns it"""
    # checking if the linked list is empty
    if linked_list.head is None:
        return
    else:
        # create a pointer to the head of the linked list
        current_node = linked_list.head
        # create a set to store the visited nodes
        visited_values = set([current_node.value])  # temporary buffer
        # create a pointer to the previous node
        previous_node = None
        # loop through the linked list
        while current_node.next:
            # checking if the next node value is in the visited set
            if current_node.next.value in visited_values:
                # if it is, remove the next node
                current_node.next = current_node.next.next
            # else add the next node value to the visited set
            else:
                visited_values.add(
                    current_node.next.value
                )  # add the next node value to the visited set
                current_node = current_node.next  # move the pointer to the next node

        return linked_list


def remove_duplicates_no_buffer(linked_list: LinkedList) -> LinkedList:
    """Remove duplicates from an unsorted linked list without using a temporary buffer and returns it"""
    # checking if the linked list is empty
    if linked_list.head is None:
        return
    else:
        # create a pointer to the head of the linked list
        current_node = linked_list.head
        # loop through the linked list
        while current_node:
            # create a pointer to the next node
            runner = current_node.next
            # looping through the rest of the linked list
            while runner:
                # checking if the next node value is equal to the current node value
                # if it is, remove the next node
                if current_node.value == runner.value:
                    current_node.next = runner.next # remove the next node
                    runner = runner.next    # move the runner pointer to the next node

                else:
                    runner = runner.next    # move the runner pointer to the next node

            # move the pointer to the next node
            current_node = current_node.next

        return linked_list


if __name__ == "__main__":

    custom_LL = LinkedList()  # create a linked list
    custom_LL.generate(
        n=10, min_value=0, max_value=9
    )  # generate a linked list with 10 nodes

    print(custom_LL)
    # remove_duplicates(custom_LL)  # remove duplicates from the linked list
    remove_duplicates_no_buffer(custom_LL)  # using no buffer
    print(custom_LL)
