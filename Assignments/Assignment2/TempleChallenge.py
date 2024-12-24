from typing import List

# Function to fetch the top element of the stack
def stackPeek(stack: List):
    # If the stack is empty, return -1
    if not stack:
        return -1
    else:
        # Return the last element of the stack (top element)
        return stack[-1]

def treasure_seq(target: List[int], n: int) -> List[str]:
    i = 1  # Counter for elements from 1 to n
    j = 0  # Counter for elements in the target list
    stack = []  # Initialize an empty stack
    output = []  # Initialize an empty output list to record operations
    
    # Loop until we have processed all elements from 1 to n or found all target elements
    while i <= n and j < len(target):
        # Push the current element onto the stack
        stack.append(i)
        output.append("Push")  # Record the operation
        
        # Check if the top of the stack matches the current target element
        if stackPeek(stack) == target[j]:
            j += 1  # Move to the next target element if there's a match
        else:
            # If there's no match, pop the top element from the stack
            stack.pop()
            output.append("Pop")  # Record the operation
        
        i += 1  # Increment the counter for the next element

    # Return the list of operations recorded in the output
    return output

# Testing the function with examples
# Uncomment to test
# print(treasure_seq([1, 3], 3))  # Output: ["Push", "Push", "Pop", "Push"]
# print(treasure_seq([1, 2, 3], 3))  # Output: ["Push", "Push", "Push"]
# print(treasure_seq([1, 2], 4))  # Output: ["Push", "Push"]
