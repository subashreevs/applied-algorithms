def longestUniformSegment(boxes: str, changes: int) -> int:
    # Helper function to determine the maximum uniform segment for a specific target character
    def max_length_with_target(target_character_under_evaluation):
        # Initialize the starting position (left boundary) of the sliding window
        left_boundary_pointer_position = 0
        # Initialize the maximum segment length encountered so far
        maximum_length_of_uniform_segment_found = 0
        # Counter to keep track of the number of modifications applied for mismatched characters
        total_count_of_character_replacement_operations = 0
        
        # Iterate through the string using the right boundary of the sliding window
        for right_boundary_pointer_position in range(len(boxes)):
            # Check if the current character differs from the target character under evaluation
            if boxes[right_boundary_pointer_position] != target_character_under_evaluation:
                # Increment the replacement counter since a mismatch occurred
                total_count_of_character_replacement_operations += 1
            
            # If the total replacements exceed the allowable change limit, adjust the window from the left
            while total_count_of_character_replacement_operations > changes:
                # Check if the character at the left boundary was contributing to the mismatch
                if boxes[left_boundary_pointer_position] != target_character_under_evaluation:
                    # Decrement the replacement counter as this character is no longer part of the window
                    total_count_of_character_replacement_operations -= 1
                # Move the left boundary to the right to reduce the window size
                left_boundary_pointer_position += 1
            
            # Calculate the current segment length within the sliding window
            current_length_of_uniform_segment = right_boundary_pointer_position - left_boundary_pointer_position + 1
            # Update the maximum length if the current segment is longer
            maximum_length_of_uniform_segment_found = max(
                maximum_length_of_uniform_segment_found, 
                current_length_of_uniform_segment
            )
        
        # Return the maximum uniform segment length achievable for the given target character
        return maximum_length_of_uniform_segment_found
    
    # Identify all unique characters in the input string to evaluate each one as a potential target character
    unique_set_of_target_characters_for_consistency = set(boxes)
    # Initialize a variable to store the longest uniform segment length found across all characters
    global_maximum_uniform_segment_length = 0
    
    # Iterate through all unique characters to calculate the maximum segment length for each target character
    for current_target_character_being_evaluated in unique_set_of_target_characters_for_consistency:
        # Update the global maximum segment length if the current target yields a longer segment
        global_maximum_uniform_segment_length = max(
            global_maximum_uniform_segment_length, 
            max_length_with_target(current_target_character_being_evaluated)
        )
    
    # Return the overall maximum uniform segment length found
    return global_maximum_uniform_segment_length

# # Test cases to verify the correctness of the function
# print(longestUniformSegment("aabbcc", 6))  # Expected Output: 6
# print(longestUniformSegment("abcbbab", 2))  # Expected Output: 6



def treasureHunt(first_parchment_sequence_of_clues, second_parchment_sequence_of_clues):
    # Ensure the longer sequence is always the first_parchment_sequence_of_clues for optimization purposes
    if len(first_parchment_sequence_of_clues) < len(second_parchment_sequence_of_clues):
        first_parchment_sequence_of_clues, second_parchment_sequence_of_clues = (
            second_parchment_sequence_of_clues, first_parchment_sequence_of_clues
        )
    
    # Determine the lengths of both parchment sequences
    total_length_of_primary_parchment = len(first_parchment_sequence_of_clues)
    total_length_of_secondary_parchment = len(second_parchment_sequence_of_clues)
    
    # Initialize a list to keep track of the previous row of common subsequences
    previous_row_of_match_lengths = [0] * (total_length_of_secondary_parchment + 1)
    
    # Variable to store the length of the longest common contiguous segment
    maximum_length_of_contiguous_matching_segment = 0
    
    # Iterate through each element in the first parchment sequence (outer loop)
    for current_index_in_primary_parchment in range(1, total_length_of_primary_parchment + 1):
        # Initialize the current row to store match lengths for this iteration
        current_row_of_match_lengths = [0] * (total_length_of_secondary_parchment + 1)
        
        # Iterate through each element in the second parchment sequence (inner loop)
        for current_index_in_secondary_parchment in range(1, total_length_of_secondary_parchment + 1):
            # Check if the current elements in both parchments are equal
            if (
                first_parchment_sequence_of_clues[current_index_in_primary_parchment - 1]
                == second_parchment_sequence_of_clues[current_index_in_secondary_parchment - 1]
            ):
                # Increment the length of the matching segment by 1 (diagonally upward)
                current_row_of_match_lengths[current_index_in_secondary_parchment] = (
                    previous_row_of_match_lengths[current_index_in_secondary_parchment - 1] + 1
                )
                
                # Update the maximum contiguous segment length found so far
                maximum_length_of_contiguous_matching_segment = max(
                    maximum_length_of_contiguous_matching_segment,
                    current_row_of_match_lengths[current_index_in_secondary_parchment],
                )
            else:
                # If elements do not match, reset the match length to 0
                current_row_of_match_lengths[current_index_in_secondary_parchment] = 0
        
        # Update the previous row to be the current row for the next iteration
        previous_row_of_match_lengths = current_row_of_match_lengths
    
    # Return the length of the longest contiguous matching segment between the two parchments
    return maximum_length_of_contiguous_matching_segment


# # Test Case 1
# first_parchment_sequence_of_clues = [5, 7, 8, 7, 5, 6]
# second_parchment_sequence_of_clues = [8, 7, 5, 3, 9]
# print(
#     "Test Case 1 Output:",
#     treasureHunt(first_parchment_sequence_of_clues, second_parchment_sequence_of_clues),
# )  # Expected Output: 3

# # Test Case 2
# first_parchment_sequence_of_clues = [1, 1, 1, 1, 1]
# second_parchment_sequence_of_clues = [1, 1, 1, 1, 1]
# print(
#     "Test Case 2 Output:",
#     treasureHunt(first_parchment_sequence_of_clues, second_parchment_sequence_of_clues),
# )  # Expected Output: 5




def findMaxLength(nums: list[int]) -> int:
    # Dictionary to store the first occurrence of each prefix sum encountered during iteration
    prefix_sum_first_occurrence_map = {}
    # Variable to keep track of the current prefix sum during traversal
    cumulative_prefix_sum_tracker = 0
    # Variable to record the maximum length of a balanced subarray found
    maximum_length_of_balanced_subarray_found = 0

    # Iterate through the array, processing each binary integer one by one
    for current_index_in_array, binary_value_in_array in enumerate(nums):
        # Update the prefix sum: increment by +1 for a '1' and decrement by -1 for a '0'
        cumulative_prefix_sum_tracker += 1 if binary_value_in_array == 1 else -1

        # If the prefix sum becomes zero, the subarray from the start to the current index is balanced
        if cumulative_prefix_sum_tracker == 0:
            maximum_length_of_balanced_subarray_found = current_index_in_array + 1
        # If the prefix sum has been encountered before, calculate the length of the balanced subarray
        elif cumulative_prefix_sum_tracker in prefix_sum_first_occurrence_map:
            subarray_length_to_evaluate = (
                current_index_in_array - prefix_sum_first_occurrence_map[cumulative_prefix_sum_tracker]
            )
            maximum_length_of_balanced_subarray_found = max(
                maximum_length_of_balanced_subarray_found, subarray_length_to_evaluate
            )
        else:
            # If the prefix sum is encountered for the first time, store its index
            prefix_sum_first_occurrence_map[cumulative_prefix_sum_tracker] = current_index_in_array

    # Return the maximum length of a balanced subarray found in the input array
    return maximum_length_of_balanced_subarray_found


# # Test Case 1: Simple balanced subarray
# nums = [0, 1]
# print(
#     "Test Case 1 Output:", findMaxLength(nums)
# )  # Expected Output: 2

# # Test Case 2: Multiple balanced segments
# nums = [0, 1, 0]
# print(
#     "Test Case 2 Output:", findMaxLength(nums)
# )  # Expected Output: 2




from typing import List, Tuple

def breaches(levels: List[int]) -> List[Tuple[int, int]]:
    # Dictionary to store prefix sums and the list of indices where they occur
    prefix_sum_to_index_map = {}
    # Variable to keep track of the cumulative prefix sum as we iterate
    cumulative_sum_of_elements_in_array = 0
    # List to store the start and end indices of all zero-sum subarrays found
    list_of_zero_sum_subarray_indices = []

    # Iterate through the array while maintaining the cumulative sum and tracking indices
    for current_index_in_array, current_element_in_levels_array in enumerate(levels):
        # Update the cumulative sum by adding the current element's value
        cumulative_sum_of_elements_in_array += current_element_in_levels_array

        # Check if the cumulative sum is zero, indicating a zero-sum subarray from the start
        if cumulative_sum_of_elements_in_array == 0:
            list_of_zero_sum_subarray_indices.append((0, current_index_in_array))

        # If the cumulative sum has been seen before, there are zero-sum subarrays ending here
        if cumulative_sum_of_elements_in_array in prefix_sum_to_index_map:
            for start_index_of_previous_sum in prefix_sum_to_index_map[cumulative_sum_of_elements_in_array]:
                list_of_zero_sum_subarray_indices.append((start_index_of_previous_sum + 1, current_index_in_array))

        # Add the current cumulative sum and its index to the dictionary if not already present
        if cumulative_sum_of_elements_in_array not in prefix_sum_to_index_map:
            prefix_sum_to_index_map[cumulative_sum_of_elements_in_array] = []
        prefix_sum_to_index_map[cumulative_sum_of_elements_in_array].append(current_index_in_array)

    # Return the list of start and end indices for all zero-sum subarrays found
    return list_of_zero_sum_subarray_indices


# # Test Case 1
# levels = [3, 4, -7, 1, 2, -6, 4, -1]
# print(
#     "Test Case 1 Output:", breaches(levels)
# )  # Expected Output: [(0, 2), (1, 4), (4, 6), (0, 7), (3, 7)]

# # Test Case 2
# levels = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
# print(
#     "Test Case 2 Output:", breaches(levels)
# )  # Expected Output: [(2, 4), (2, 6), (5, 6), (6, 9), (0, 10)]
