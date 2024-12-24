def rearrangeAllToys(toy_list):
    # Sort the toys array
    toy_list.sort()
    total_toys = len(toy_list)
    
    # Create a new array to store the rearranged toys
    rearranged_toys = [0] * total_toys
    
    # Find the middle index and set up two pointers
    middle_index = (total_toys + 1) // 2
    left_pointer = middle_index - 1  # Pointer for smaller elements
    right_pointer = total_toys - 1     # Pointer for larger elements
    
    # Use a while loop to fill the rearranged array in a zig-zag pattern
    index = 0  # Initialize index for the rearranged array
    while index < total_toys:
        if index % 2 == 0:
            # Even index: take from the left (smaller elements)
            rearranged_toys[index] = toy_list[left_pointer]
            left_pointer -= 1  # Move left pointer to the left
        else:
            # Odd index: take from the right (larger elements)
            rearranged_toys[index] = toy_list[right_pointer]
            right_pointer -= 1  # Move right pointer to the left
        
        index += 1  # Increment index to move to the next position
    
    return rearranged_toys

# Example usage
# toys1 = [1, 5, 1, 1, 6, 4]
# print(rearrangeAllToys(toys1))  # Output: [1, 6, 1, 5, 1, 4]

# toys2 = [1, 3, 2, 2, 3, 1]
# print(rearrangeAllToys(toys2))  # Output: [2, 3, 1, 3, 1, 2]
