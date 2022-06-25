# Implement Queue class which implements a queue using two stacks

class Stack:
    def __init__(self) -> None:
        self.list = []
        
    def __len__(self):
        """Returns the length of stack"""
        return len(self.list)
    
    def push(self, item):
        """Add item to the the stack"""
        self.list.append(item)
        
    def pop(self):
        """Removes the last item from the stack"""
        if len(self.list) == 0:
            return None
        
        return self.list.pop()
        
    
class QueueViaStack:
    def __init__(self):
        """Initializes two stacks"""
        self.in_stack = Stack() # main stack, to enqueue
        self.out_stack = Stack()    # to dequeue
    
    def enqueue(self, item):
        """Adds an element to the queue"""
        self.in_stack.push(item=item)
        
        
    def dequeue(self):
        """Removes the first element of the queue and returns it"""
        # move the items from in_stack to out_stack in reverse order
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        
        # remove the last element of the out_stack, ie. first element of the queue
        result = self.out_stack.pop()
        
        # move the items from out_stack to in_stack
        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
            
        return result
    
    
if __name__ == "__main__":
    
    custom_queue = QueueViaStack()
    
    custom_queue.enqueue(1)
    custom_queue.enqueue(2)
    custom_queue.enqueue(3)
    print(custom_queue.dequeue())
    custom_queue.enqueue(4)
    print(custom_queue.dequeue())
    
    