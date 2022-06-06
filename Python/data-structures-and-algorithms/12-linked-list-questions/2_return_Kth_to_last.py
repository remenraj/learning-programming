# Program to find the nth to last element of a singly linked list
# time complexity: O(n)
# space complexity: O(1)

from linked_list import LinkedList


def nth_to_last(linked_list: LinkedList, n: int) -> int:
    """Returns the value of nth node from the end of the linked list"""
    # check if the linked list is empty
    if linked_list is None:
        return None

    # create two pointers, both pointing to the head of the linked list
    # after iteration, pointer1 will be at the nth node from the end
    pointer1 = linked_list.head
    pointer2 = linked_list.head
    
    # move the pointer2 to the nth node from head
    for _ in range(n):  # range(n) executes (n-1) times
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    
    # move the pointer1 and pointer2 pointers until pointer2 reaches the end
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1


if __name__ == "__main__":
    
    custom_LL = LinkedList()  # create a linked list
    custom_LL.generate(
        n=10, min_value=0, max_value=9
    )  # generate a linked list with 10 nodes

    print(custom_LL)
    print(nth_to_last(custom_LL, n=3))  # print the 3rd node from the end