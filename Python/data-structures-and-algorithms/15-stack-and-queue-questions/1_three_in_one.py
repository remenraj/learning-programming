# Describe how you could use a single python list to implement three stacks.


class MultiStack:
    def __init__(self, stack_size: int) -> None:
        """Initialize the stack with a stack size."""
        self.total_stacks = 3  # number of stacks
        self.stack_size = stack_size  # stack size, total elements in each stack
        self.custom_list = [None] * (
            self.total_stacks * self.stack_size
        )  # list of stacks

        # size_of_stacks list keeps track of the size of each stack,
        # which is updated when operations are performed on the stack.
        # each stack is numbered: stack_num: 0, 1, 2, .., self.total_stacks
        self.size_of_stacks = [0] * self.total_stacks

    def is_full(self, stack_num: int) -> bool:
        """Check if the stack is full."""
        # if the stack is full, then the size of the stack is equal to the stack size.
        return self.size_of_stacks[stack_num] == self.stack_size

    def is_empty(self, stack_num: int) -> bool:
        """Check if the stack is empty"""
        #  if the size of stack is zero, then it is empty
        return self.size_of_stacks[stack_num] == 0

    def index_of_top(self, stack_num: int) -> int:
        """Return the index of the top element of the stack."""
        offset = stack_num * self.stack_size    # offset is the index of the bottom element of the stack/first element of the stack

        if self.is_empty(stack_num):
            return offset
        else:
            return offset + self.size_of_stacks[stack_num] - 1
    
    def push(self, item, stack_num: int):
        """Push an item to the stack."""
        if self.is_full(stack_num):
            # raise Exception("Stack is full")
            return "Stack is full"
        else:
            # update the size of the current stack
            self.size_of_stacks[stack_num] += 1
            
            # Add the item to the stack
            self.custom_list[self.index_of_top(stack_num)] = item
            
            return item

    def pop(self, stack_num: int):
        """Removes the top item from the specified stack"""
        if self.is_empty(stack_num):
            # raise Exception("Stack is empty")
            return "Stack is empty"
        else:
            item = self.custom_list[self.index_of_top(stack_num)]   # to return the popped value
            
            # remove the top item from the stack
            self.custom_list[self.index_of_top(stack_num)] = None
            
            # update the size of the current stack
            self.size_of_stacks[stack_num] -= 1
            
            return item
            
    def peek(self, stack_num: int):
        """ Returns the top value of the specified stack """
        if self.is_empty(stack_num):
            return "The stack is empty"
        else:
            return self.custom_list[self.index_of_top(stack_num)]
                
        
customStack = MultiStack(4)

print(customStack.push(1, stack_num=0))
print(customStack.push(2, stack_num=2))
print(customStack.push(2, stack_num=1))
print(customStack.push(2, stack_num=1))
print(customStack.push(2, stack_num=0))
print(customStack.push(3, stack_num=2))
print(customStack.pop(0))
print(customStack.is_empty(stack_num=2))
print(customStack.custom_list)