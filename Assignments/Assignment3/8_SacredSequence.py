def sacred_sequence(keys: int, position: int) -> str:
    from math import factorial
    
    # Create a list of numbers from 1 to keys
    numbers = list(range(1, keys + 1))
    
    # Adjust position for 0-based index
    k = position - 1
    
    result = []
    
    # Build the k-th permutation
    for i in range(keys, 0, -1):
        # Determine the factorial of the current number of remaining elements
        fact = factorial(i - 1)
        
        # Determine the index of the current number to use
        index = k // fact
        
        # Append the chosen number to the result
        result.append(str(numbers[index]))
        
        # Remove the used number from the list
        numbers.pop(index)
        
        # Reduce k for the next position
        k %= fact
    
    return ''.join(result)

# Test Cases
# print(sacred_sequence(3, 3))  # Output: "213"
# print(sacred_sequence(4, 9))  # Output: "2314"
