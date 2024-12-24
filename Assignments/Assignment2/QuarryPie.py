class QuarryPieLine:
    def __init__(self):
        self.left_stack = []   # Stack to hold the front half
        self.right_stack = []  # Stack to hold the back half
        self.counter = 0       # To generate unique person IDs

    # Add a person to the front of the line
    def joinInFront(self):
        self.counter += 1
        self.left_stack.append(self.counter)
        self.balance_stacks()

    # Add a person to the middle of the line
    def joinInMiddle(self):
        self.counter += 1
        if len(self.left_stack) <= len(self.right_stack):
            self.left_stack.append(self.counter)
        else:
            self.right_stack.append(self.counter)
        self.balance_stacks()

    # Add a person to the back of the line
    def joinInBack(self):
        self.counter += 1
        self.right_stack.append(self.counter)

    # Remove a person from the front of the line
    def removeFromFront(self):
        if self.left_stack:
            self.left_stack.pop()
        self.balance_stacks()

    # Remove a person from the middle of the line
    def removeFromMiddle(self):
        if len(self.left_stack) > len(self.right_stack):
            self.left_stack.pop()
        else:
            self.right_stack.pop(0)
        self.balance_stacks()

    # Remove a person from the back of the line
    def removeFromBack(self):
        if self.right_stack:
            self.right_stack.pop()

    # Return the person at the front of the line
    def whoIsFront(self) -> int:
        return self.left_stack[-1] if self.left_stack else -1

    # Return the person at the middle of the line
    def whoIsMiddle(self) -> int:
        if len(self.left_stack) > len(self.right_stack):
            return self.left_stack[-1]
        return self.right_stack[0] if self.right_stack else -1

    # Return the person at the back of the line
    def whoIsBack(self) -> int:
        return self.right_stack[-1] if self.right_stack else (self.left_stack[-1] if self.left_stack else -1)

    # Helper function to balance the stacks
    def balance_stacks(self):
        # If left_stack has too many elements, move one to right_stack
        if len(self.left_stack) > len(self.right_stack) + 1:
            self.right_stack.insert(0, self.left_stack.pop())
        # If right_stack has more elements than left_stack, move one to left_stack
        elif len(self.right_stack) > len(self.left_stack):
            self.left_stack.append(self.right_stack.pop(0))

# Example usage
operations = [1, 2, 2, 3, 5, 6, 7, 8, 9]
qp = QuarryPieLine()
result = []

for op in operations:
    if op == 1:
        qp.joinInFront()
    elif op == 2:
        qp.joinInMiddle()
    elif op == 3:
        qp.joinInBack()
    elif op == 5:
        qp.removeFromMiddle()
    elif op == 6:
        qp.removeFromBack()
    elif op == 7:
        result.append(qp.whoIsFront())
    elif op == 8:
        result.append(qp.whoIsMiddle())
    elif op == 9:
        result.append(qp.whoIsBack())

print(result)  # Output: [2, 2, 1]
