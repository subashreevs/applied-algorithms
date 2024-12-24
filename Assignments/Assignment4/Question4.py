def magical_recipe(total_cases: int, binary_strings: list[str]) -> list[int]:
    MODULO_PRIME = 998244353  # Large prime number to handle exponential growth and prevent overflow
    result_list = []  # List to store results for each test case

    # Process each test case individually
    for binary_string in binary_strings:
        string_length = len(binary_string)  # Length of the binary string for this test case
        # Initialize a dynamic programming array with zeros, where ad[i] stores the number of ways up to i
        ways_to_map_binary_string = [0] * (string_length + 1)
        ways_to_map_binary_string[0] = 1  # Base case: there is 1 way to have an empty initial binary string

        # Iterate over each character in the binary string
        for current_position in range(1, string_length + 1):
            # Case where we map a single 'a' or 'b' in the binary string
            if current_position >= 1:
                if binary_string[current_position - 1] == 'a':
                    # Update the current position by adding the previous position's value
                    ways_to_map_binary_string[current_position] = (
                        ways_to_map_binary_string[current_position] + ways_to_map_binary_string[current_position - 1]
                    ) % MODULO_PRIME  # Single character 'a' (from '01' mapping)
                
                elif binary_string[current_position - 1] == 'b':
                    # Update the current position by adding the previous position's value
                    ways_to_map_binary_string[current_position] = (
                        ways_to_map_binary_string[current_position] + ways_to_map_binary_string[current_position - 1]
                    ) % MODULO_PRIME  # Single character 'b' (from '10' mapping)
            
            # Case where we map two characters 'ab' or 'ba' in the binary string
            if current_position >= 2:
                if binary_string[current_position - 2:current_position] == 'ab':
                    # Update the current position by adding the value from two positions back
                    ways_to_map_binary_string[current_position] = (
                        ways_to_map_binary_string[current_position] + ways_to_map_binary_string[current_position - 2]
                    ) % MODULO_PRIME  # Two characters 'ab' (from '010' mapping)
                
                elif binary_string[current_position - 2:current_position] == 'ba':
                    # Update the current position by adding the value from two positions back
                    ways_to_map_binary_string[current_position] = (
                        ways_to_map_binary_string[current_position] + ways_to_map_binary_string[current_position - 2]
                    ) % MODULO_PRIME  # Two characters 'ba' (from '101' mapping)
        
        # Append the final result for this binary string to the result list
        result_list.append(ways_to_map_binary_string[string_length])

    return result_list  # Return the results for all test cases


# # Example usage
# T = 3
# cases = ["ab", "aa", "abb"]
# print(magical_recipe(T, cases))  # Output: [2, 1, 2]

# # Additional test cases
# T2 = 2
# cases2 = ["aaaa", "bbb"]
# print(magical_recipe(T2, cases2))  # Output: [1, 1]
