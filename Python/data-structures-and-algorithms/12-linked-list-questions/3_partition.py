# Program to partition a linked list around a value x, 
# such that all nodes less than x come before all nodes greater than or equal to x.
# time complexity: O(n)
# space complexity: O(1)

from linked_list import LinkedList


def partition(linked_list: LinkedList, x: int):
    """Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x"""
    # checking if the linked list is empty
    if linked_list is None:
        return None
    else:
        # create a temporary node and set it to the head of the linked list
        current_node = linked_list.head 
        linked_list.tail = linked_list.head # set the tail to the head
        
        # 
        while current_node:
            next_node = current_node.next   # create a pointer to the next node
            
            current_node.next = None    # set the next reference of the current node to None
            
            # checking if the current node value is less than x
            if current_node.value < x:
                current_node.next = linked_list.head    #
                linked_list.head = current_node
            else:
                linked_list.tail.next = current_node
                linked_list.tail = current_node

            current_node = next_node

        # setting the next reference of tail to None if it is not None
        if linked_list.tail.next is not None:
            linked_list.tail.next = None
        
    
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.generate(n=10, min_value=0, max_value=99)
    print(linked_list)
    partition(linked_list, 40)
    print(linked_list)