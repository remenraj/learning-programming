# Imagine a stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a
# new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
# set_of_stacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity,
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return
# the same values as it would if there were just a single stack).
# Implement a function popAt(int index) which performs a pop operation on a specific sub - stack.


class PlateStack:
    def __init__(self, capacity) -> None:
        self.capacity = capacity  # capacity of single stack
        self.stacks = []

    def __str__(self):
        if len(self.stacks) == 0:
            return "Stack is empty"

        else:
            stack_string = []
            for i in range(len(self.stacks)):
                for j in range(len(self.stacks[i])):
                    # print(self.stacks[i][j], end=" ")
                    stack_string.append(str(self.stacks[i][j]))

                stack_string.append("\n")

            return " ".join(stack_string)

    def push(self, item: int):
        """Add an item to the stack"""
        # check if the stacks is not empty and the last stack has not reached capacity
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            # add item to the last stack
            self.stacks[-1].append(item)

        else:
            # add item new stack in stacks (this also takes care of stacks when its empty)
            self.stacks.append([item])

    def pop(self):
        """Removes the last item in the stack"""
        # check if there are items in stacks and the last stack is empty (empty list), then remove that empty list
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()

        # check if the stack is empty, then return None
        if len(self.stacks) == 0:
            return None
        else:
            # remove the last item from the stack
            return self.stacks[-1].pop()

    def pop_at(self, stack_num: int):
        """Removes the last item from the specified stack"""
        # check if there are elements to remove in the specified stack
        if len(self.stacks[stack_num]) > 0:
            # remove the last item from the stack
            return self.stacks[stack_num].pop()

        else:
            return None


if __name__ == "__main__":
    custom_stack = PlateStack(capacity=2)

    custom_stack.push(1)
    custom_stack.push(2)
    custom_stack.push(3)
    custom_stack.push(4)
    custom_stack.push(5)
    print(custom_stack)

    custom_stack.pop()

    print(custom_stack)

    custom_stack.pop_at(stack_num=0)

    print(custom_stack)
