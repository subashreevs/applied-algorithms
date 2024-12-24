from collections import deque  # Import deque for efficient queue-based operations

# Define a Node class to represent each node in the wavelet tree
class Node:
    def __init__(self, bitmap_data_for_node=None, left_child_node_reference=None, right_child_node_reference=None):
        self.data = bitmap_data_for_node  # Store bitmap data at this node
        self.left = left_child_node_reference  # Reference to the left child node
        self.right = right_child_node_reference  # Reference to the right child node

# Define a Wavelet_Tree class to manage and build the wavelet tree structure
class Wavelet_Tree:
    def __init__(self, initial_data_array_to_process: list[int] = []):
        # Check if an initial array is provided and start the wavelet tree construction
        if initial_data_array_to_process:
            # Build the wavelet tree using the provided array and root node
            self.root_node_reference = self.build_wavelet_tree(initial_data_array_to_process, 
                                                               minimum_value_in_array=min(initial_data_array_to_process), 
                                                               maximum_value_in_array=max(initial_data_array_to_process))
            # Store the original data array for future reference and operations
            self.original_input_data_array = initial_data_array_to_process
        else:
            # If no initial array is provided, set the root and array to None
            self.root_node_reference = None
            self.original_input_data_array = []

    # Method to recursively build the wavelet tree
    def build_wavelet_tree(self, data_array_segment, minimum_value_in_array, maximum_value_in_array):
        # Base condition for recursion: If the range has converged, create a leaf node
        if minimum_value_in_array == maximum_value_in_array:
            return Node('X' * len(data_array_segment))  # Create a leaf node with placeholder 'X'

        # Calculate the midpoint for dividing the array segment in half
        midpoint_value_in_range = (minimum_value_in_array + maximum_value_in_array) // 2
        left_partition_subarray = []  # Initialize array to store elements for the left partition
        right_partition_subarray = []  # Initialize array to store elements for the right partition
        bitmap_representation_for_current_node = []  # Initialize bitmap for the current node

        # Traverse through each element in the current data segment
        for individual_element_in_array in data_array_segment:
            # Check if the element belongs to the left partition
            if individual_element_in_array <= midpoint_value_in_range:
                bitmap_representation_for_current_node.append('0')  # Append '0' for left partition
                left_partition_subarray.append(individual_element_in_array)  # Add element to left subarray
            else:
                # Element belongs to the right partition
                bitmap_representation_for_current_node.append('1')  # Append '1' for right partition
                right_partition_subarray.append(individual_element_in_array)  # Add element to right subarray

        # Create the current node with the constructed bitmap string
        current_wavelet_tree_node = Node(''.join(bitmap_representation_for_current_node))
        
        # Recursively build the left child node if the left partition is not empty
        if left_partition_subarray:
            current_wavelet_tree_node.left = self.build_wavelet_tree(left_partition_subarray, 
                                                                     minimum_value_in_array, 
                                                                     midpoint_value_in_range)
        # Recursively build the right child node if the right partition is not empty
        if right_partition_subarray:
            current_wavelet_tree_node.right = self.build_wavelet_tree(right_partition_subarray, 
                                                                      midpoint_value_in_range + 1, 
                                                                      maximum_value_in_array)
        return current_wavelet_tree_node  # Return the created node as part of the recursive build

    # Method to retrieve the level order traversal of the wavelet tree
    def get_wavelet_level_order(self):
        # Return an empty list if there is no root node
        if not self.root_node_reference:
            return []

        # List to store the wavelet tree's levels in order
        wavelet_tree_level_order_representation = []
        # Initialize a queue for level-order traversal starting with the root node
        node_traversal_queue = deque([self.root_node_reference])

        # Continue traversing until the queue is empty
        while node_traversal_queue:
            # List to store the data at nodes on the current level
            current_level_node_data = []
            # Process each node at the current level
            for _ in range(len(node_traversal_queue)):
                # Remove the front node from the queue for processing
                current_wavelet_tree_node = node_traversal_queue.popleft()
                
                # Check if the node is valid and add its data
                if current_wavelet_tree_node:
                    # Append the bitmap data of the current node to the current level list
                    current_level_node_data.append(current_wavelet_tree_node.data)
                    
                    # Add left and right children to the queue for the next level, if they exist
                    if current_wavelet_tree_node.left or current_wavelet_tree_node.right:
                        node_traversal_queue.append(current_wavelet_tree_node.left)
                        node_traversal_queue.append(current_wavelet_tree_node.right)
            
            # Add the current level data to the final level order representation
            wavelet_tree_level_order_representation.append(current_level_node_data)
        
        return wavelet_tree_level_order_representation  # Return the complete level order of the wavelet tree

    # Method to count occurrences of a target character up to a given position
    def rank(self, target_character_to_find, target_position_limit):
        # Check if the target character is out of bounds for the given array
        if not self.root_node_reference or target_character_to_find < min(self.original_input_data_array) or \
           target_character_to_find > max(self.original_input_data_array):
            return 0  # Return zero occurrences if character is out of valid range

        # Initialize a counter for occurrences of the target character
        character_occurrence_counter = 0

        # Traverse the original array up to the target position
        for current_index_in_array in range(target_position_limit):
            # Check if the character at current position matches the target
            if self.original_input_data_array[current_index_in_array] == target_character_to_find:
                # Increment counter if character matches
                character_occurrence_counter += 1

        return character_occurrence_counter  # Return the total count of target character occurrences

# # Instantiate the Wavelet_Tree class with a sample array and display level order
# wv_tree = Wavelet_Tree([6, 2, 0, 7, 9, 3, 1, 8, 5, 4])
# print(wv_tree.get_wavelet_level_order())  # Print the wavelet tree's level-order structure
# # Expected output: [['1001100110'], ['00101', '00110'], ['100', '01', '010', '10'], ['01', 'X', 'X', 'X', '10', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]

# # Test the rank function to find occurrences of 7 up to the 3rd position
# print(wv_tree.rank(7, 3))  # Expected output: 0

# # Instantiate the Wavelet_Tree class with another sample array and display level order
# wv_tree = Wavelet_Tree([6, 2, 0, 7, 7, 9, 3, 1, 8, 5, 4])
# print(wv_tree.get_wavelet_level_order())  # Print the wavelet tree's level-order structure
# # Expected output: [['10011100110'], ['00101', '000110'], ['100', '01', '0110', '10'], ['01', 'X', 'X', 'X', '10', 'XX', 'X', 'X'], ['X', 'X', 'X', 'X']]

# # Test the rank function to find occurrences of 7 up to the 5th position
# print(wv_tree.rank(7, 5))  # Expected output: 2
