def endgameScores(points: list[int]) -> bool:
    # Get the number of points (games)
    num_points = len(points)

    # Create a 2D DP array initialized to 0
    dp_table = [[0] * num_points for _ in range(num_points)]
    
    # Base case: when there's only one game available
    index = 0
    while index < num_points:
        dp_table[index][index] = points[index]  # Initialize the diagonal
        index += 1

    # Fill the DP table for all possible lengths of subarrays
    length = 2  # Start with a length of 2
    while length <= num_points:  # Length of the subarray
        starting_index = 0  # Initialize starting index of the subarray
        while starting_index <= num_points - length:  # Loop to find all subarrays of current length
            ending_index = starting_index + length - 1  # Calculate the ending index
            
            # Calculate the score difference for current subarray
            dp_table[starting_index][ending_index] = max(
                points[starting_index] - dp_table[starting_index + 1][ending_index],  # Pick the start
                points[ending_index] - dp_table[starting_index][ending_index - 1]     # Pick the end
            )
            
            starting_index += 1  # Move to the next starting index
        
        length += 1  # Move to the next length of subarrays
    
    # Ronaldo wins or ties if the score difference is non-negative
    return dp_table[0][num_points - 1] >= 0

# Test Cases
# print(endgameScores([3, 99, 155, 8]))  # Output: True
# print(endgameScores([5, 1, 100, 1, 5]))  # Output: False