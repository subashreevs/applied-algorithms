def heavenGates(scroll1, scroll2, scroll3):
    # Check if the combined length of scroll1 and scroll2 matches scroll3; if not, interleaving is impossible
    if len(scroll1) + len(scroll2) != len(scroll3):
        return False  # Return False as interleaving cannot be achieved
    
    # Initialize a 2D DP (dynamic programming) table with False values
    interleaving_possible_table = [[False] * (len(scroll2) + 1) for _ in range(len(scroll1) + 1)]
    
    # Set the base case: True if both scroll1 and scroll2 are empty and form an empty scroll3
    interleaving_possible_table[0][0] = True  
    
    # Fill the DP table to check possible interleaving
    for scroll1_index in range(len(scroll1) + 1):
        for scroll2_index in range(len(scroll2) + 1):
            # Check if the character from scroll1 can contribute to the current cell in the DP table
            if scroll1_index > 0 and scroll1[scroll1_index - 1] == scroll3[scroll1_index + scroll2_index - 1]:
                # Update the current cell based on previous value in scroll1's direction
                interleaving_possible_table[scroll1_index][scroll2_index] = interleaving_possible_table[scroll1_index][scroll2_index] or interleaving_possible_table[scroll1_index - 1][scroll2_index]
            
            # Check if the character from scroll2 can contribute to the current cell in the DP table
            if scroll2_index > 0 and scroll2[scroll2_index - 1] == scroll3[scroll1_index + scroll2_index - 1]:
                # Update the current cell based on previous value in scroll2's direction
                interleaving_possible_table[scroll1_index][scroll2_index] = interleaving_possible_table[scroll1_index][scroll2_index] or interleaving_possible_table[scroll1_index][scroll2_index - 1]
    
    # The result is whether we can interleave all of scroll1 and scroll2 to form scroll3
    return interleaving_possible_table[len(scroll1)][len(scroll2)]

# # Test cases
# print(heavenGates("aacbcc", "bbbaccaa", "aacbbbcbacccaa"))  # Expected output: True
# print(heavenGates("aabcc", "dbbca", "aadbbbaccc"))          # Expected output: False
# print(heavenGates("", "", ""))                              # Expected output: True