def beautifulNinjaFormation(n: int) -> list[int]:
    # Base cases: return specific formations for n = 1 and n = 2
    if n == 1:
        return [1]  # Only one ninja, formation is [1]
    elif n == 2:
        return [1, 2]  # Two ninjas, formation is [1, 2]

    # Recursively generate beautiful ninja formation for odds and evens
    # Recursion ensures that no ninja satisfies 2 * nums[k] = nums[i] + nums[j]
    odd_count = (n + 1) // 2  # Count of odd-indexed elements
    even_count = n // 2       # Count of even-indexed elements
    
    # Generate odd-indexed elements
    odd_ninjas = beautifulNinjaFormation(odd_count)  # Odd-indexed elements
    # Generate even-indexed elements
    even_ninjas = beautifulNinjaFormation(even_count)  # Even-indexed elements

    # Initialize the result list
    result = []
    
    # Add the scaled odd ninjas to the result using a while loop
    index = 0  # Initialize the index for odd ninjas
    while index < len(odd_ninjas):
        result.append(2 * odd_ninjas[index] - 1)  # Scale and append odd ninja
        index += 1  # Move to the next odd ninja

    # Add the scaled even ninjas to the result using a while loop
    index = 0  # Initialize the index for even ninjas
    while index < len(even_ninjas):
        result.append(2 * even_ninjas[index])  # Scale and append even ninja
        index += 1  # Move to the next even ninja

    return result

# Test cases
# print(beautifulNinjaFormation(4))  # Example output: [1, 3, 2, 4]
# print(beautifulNinjaFormation(5))  # Example output: [1, 5, 3, 2, 4]