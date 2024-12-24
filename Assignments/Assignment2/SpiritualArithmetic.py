def spiritualArithmetic(incantation: list[str]) -> int:
    # Initialize an empty stack to hold numbers
    stack = []
    
    if(len(incantation) == 1):
        return int(incantation[0])

    # Iterate through each token in the input list
    for i in incantation:
      
        # Check if the current token is an operator
        if i in "+-/*":
            # Pop the top two numbers from the stack for the operation
            int2 = int(stack.pop())  # Second operand
            int1 = int(stack.pop())  # First operand

            # Perform the appropriate operation based on the operator
            if i == '+':
                res = int1 + int2  # Addition
            elif i == "-":
                res = int1 - int2  # Subtraction
            elif i == "/":
                res = int(int1/int2)  # Division
            elif i == "*":
                res = int1 * int2  # Multiplication
            
            # Push the result of the operation back onto the stack
            stack.append(res)
        else:
            # If the token is a number, convert it to an integer and push it onto the stack
            stack.append(i)
        
        # Print the current state of the stack for debugging purposes
        print(stack)

    # The final result will be the only element left in the stack
    return stack[0]

# Example usage
# Uncomment to test
# print(spiritualArithmetic(["2", "1", "+", "3", "*"]))  # Expected output: 9
# print(spiritualArithmetic(["4", "13", "5", "/", "+"]))  # Expected output: 6
# print(spiritualArithmetic(["10", "6", "9", "3", "+", "-11", "*", "/", "17", "+", "5", "+"]))  # Expected output: 22


