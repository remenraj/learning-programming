# Sum Lists
# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1 's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.

# Example:
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295 = 912.
# Output: 2 -> 1 -> 9. That is, 912.


# time complexity: O(n)
# space complexity: O(n)

from platform import node
from linked_list import LinkedList


def sum_lists(ll_a: LinkedList, ll_b: LinkedList) -> LinkedList:
    
    # if one of the linked lists is empty, return the other linked list
    if len(ll_a) == 0:
        return ll_b
    if len(ll_b) == 0:
        return ll_a

    # nodes
    node_1 = ll_a.head
    node_2 = ll_b.head
    
    # create a new linked list to store the sum of the two linked lists
    ll_sum = LinkedList()
    # initialize a variable to store the carry over
    carry_over = 0
    
    # iterate over the linked lists
    while node_1 or node_2:
        
        sum = carry_over
        
        if node_1:
            sum += node_1.value
            node_1 = node_1.next
        
        if node_2:
            sum += node_2.value
            node_2 = node_2.next
        
        # add the sum to the linked list
        ll_sum.add(sum % 10)
        
        # update the carry over
        carry_over = sum // 10
        
    return ll_sum


if __name__ == "__main__":
    
    ll_1 = LinkedList()
    ll_1.add(7)
    ll_1.add(1)
    ll_1.add(6)
    print(ll_1)
    print("+")
    
    ll_2 = LinkedList()
    ll_2.add(5)
    ll_2.add(9)
    ll_2.add(2)
    print(ll_2)
    print("=")
    
    print(sum_lists(ll_1, ll_2))
    