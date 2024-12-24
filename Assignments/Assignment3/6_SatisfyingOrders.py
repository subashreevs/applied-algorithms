def satisfyingOrders(total_people: int, satisfied_people: int) -> int:
    MOD = 10**9 + 7  # Define the modulus for calculations

    # Create a DP table with (total_people + 1) x (satisfied_people + 1)
    dp_table = [[0] * (satisfied_people + 1) for _ in range(total_people + 1)]
    
    # Base case: One person can satisfy themselves
    dp_table[1][1] = 1  

    # Fill the DP table
    current_people = 2  # Start from 2 people
    while current_people <= total_people:  # Loop for the number of people
        current_satisfied = 1  # Start with 1 satisfied person
        while current_satisfied <= satisfied_people:  # Loop for the number of satisfied people
            # If the new person is satisfied
            dp_table[current_people][current_satisfied] = dp_table[current_people - 1][current_satisfied - 1]  # Last person satisfied
            
            # If the new person is not satisfied
            dp_table[current_people][current_satisfied] += (current_people - 1) * dp_table[current_people - 1][current_satisfied]
            dp_table[current_people][current_satisfied] %= MOD
            
            current_satisfied += 1  # Move to the next number of satisfied people
        
        current_people += 1  # Move to the next number of people

    return dp_table[total_people][satisfied_people]  # Return the result for total_people and satisfied_people

# Test Cases
# print(satisfyingOrders(4, 3))  # Output: 6
# print(satisfyingOrders(5, 2))  # Example case for testing