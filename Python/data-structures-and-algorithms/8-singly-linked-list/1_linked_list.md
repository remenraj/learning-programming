**Linked List**
Linked list is a form of sequential collection and it does not have to be in order.
A linked list is made up of independent nodes that may contain any type of data and each node has a reference to the next node in the link.
First node is called head and last node is called tail.
First node contains Head and reference to the next node
Last node, Tail contains data and no reference(null)


**Linked List vs Array**

Elements of linked list are independent objects (stored in non-contiguous memory locations) vs elements of array are stored in contiguous memory locations.
The size of linked list is not pre allocated vs array is pre allocated.
Insertion and removal of elements in linked list are very efficient because they do not require shifting of other elements.
Random access - accessing an element in arrays is very efficient
Random access in linked list is very inefficient because it requires traversing of the list to find the element.


**Types of Linked List**

- Singly Linked List: each node stores data and has a reference to the next node in the list, except the last node which has no reference(null).
- Circular Singly Linked List: each node stores data and has a reference to the next node in the list, and the last node has a reference to the first node.
    e.g.: 4 player chess
- Doubly Linked List: each node stores data and has reference to the previous node and the next node, except the last node which has reference to the last node and no reference(null) to the next node.
    e.g.: Music Player
- Circular Doubly Linked List: each node stores data and has reference to the previous node and the next node, except the last node which has reference to the last node and reference to the next node is the first node.
    e.g.: switching between apps in windows [ctrl + tab]
    


    
