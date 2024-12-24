from collections import deque  # Import deque for managing queue-based operations efficiently in the wavelet tree structure

# Define a Node class to represent individual nodes within the wavelet tree structure
class Node:
    def __init__(self, bitmap_data_for_node=None, left_child_node_reference=None, right_child_node_reference=None):
        self.data = bitmap_data_for_node  # Stores bitmap data that represents the partitioning at this node
        self.left = left_child_node_reference  # Stores a reference to the left child node of the current node
        self.right = right_child_node_reference  # Stores a reference to the right child node of the current node

# Define a Wavelet_Tree class to handle and manage the construction and traversal of the wavelet tree
class Wavelet_Tree:
    def __init__(self, initial_data_array_to_process: list[int] = []):
        # If an initial data array is provided, start building the wavelet tree immediately
        if initial_data_array_to_process:
            # Construct the wavelet tree by passing the data array and determining the minimum and maximum values within it
            self.root_node_reference = self.build_wavelet_tree(
                initial_data_array_to_process,
                minimum_value_in_array=min(initial_data_array_to_process),
                maximum_value_in_array=max(initial_data_array_to_process),
            )
            # Store the original array for any reference or processing that may be required later
            self.original_input_data_array = initial_data_array_to_process
        else:
            # If no initial data is provided, set the root and array references to None
            self.root_node_reference = None
            self.original_input_data_array = []

    # Recursive function to build the wavelet tree by partitioning values based on a midpoint value
    def build_wavelet_tree(self, data_array_segment, minimum_value_in_array, maximum_value_in_array):
        # The base case for recursion: if min and max values are the same, create a leaf node without any further partitioning
        if minimum_value_in_array == maximum_value_in_array:
            return Node('X' * len(data_array_segment))  # Leaf nodes are represented by placeholder bitmaps such as 'X'

        # Calculate the midpoint of the range to determine how the array should be partitioned
        midpoint_value_in_range = (minimum_value_in_array + maximum_value_in_array) // 2
        left_partition_subarray = []  # List to collect elements for the left partition based on the midpoint
        right_partition_subarray = []  # List to collect elements for the right partition based on the midpoint
        bitmap_representation_for_current_node = []  # Bitmap representing the current node's partition decisions

        # Loop through each element in the segment, checking if it falls into the left or right partition
        for individual_element_in_array in data_array_segment:
            # Elements less than or equal to the midpoint go to the left partition and get a '0' in the bitmap
            if individual_element_in_array <= midpoint_value_in_range:
                bitmap_representation_for_current_node.append('0')
                left_partition_subarray.append(individual_element_in_array)
            else:
                # Elements greater than the midpoint go to the right partition and get a '1' in the bitmap
                bitmap_representation_for_current_node.append('1')
                right_partition_subarray.append(individual_element_in_array)

        # Create the node for the current segment with the generated bitmap string representation
        current_wavelet_tree_node = Node(''.join(bitmap_representation_for_current_node))

        # Recursively build the left child node if there are elements in the left partition
        if left_partition_subarray:
            current_wavelet_tree_node.left = self.build_wavelet_tree(
                left_partition_subarray,
                minimum_value_in_array,
                midpoint_value_in_range,
            )
        # Recursively build the right child node if there are elements in the right partition
        if right_partition_subarray:
            current_wavelet_tree_node.right = self.build_wavelet_tree(
                right_partition_subarray,
                midpoint_value_in_range + 1,
                maximum_value_in_array,
            )
        # Return the constructed node so that it becomes part of the recursive tree construction
        return current_wavelet_tree_node

    # Method to obtain the wavelet tree's structure in level order, helpful for visualization
    def get_wavelet_level_order(self):
        # If there is no root, return an empty list since the tree is empty
        if not self.root_node_reference:
            return []

        # Initialize the final representation of each level in the wavelet tree as an empty list
        wavelet_tree_level_order_representation = []
        # Initialize a queue with the root node to begin level-order traversal from the top
        node_traversal_queue = deque([self.root_node_reference])

        # Loop until there are no more nodes to process in the queue
        while node_traversal_queue:
            # Temporary list to store data for the current level being processed
            current_level_node_data = []
            # Process each node in the current level by dequeuing it from the queue
            for _ in range(len(node_traversal_queue)):
                # Pop the node at the front of the queue to process its data and children
                current_wavelet_tree_node = node_traversal_queue.popleft()

                # If the node exists, store its data and enqueue its children (if any) for processing in the next level
                if current_wavelet_tree_node:
                    current_level_node_data.append(current_wavelet_tree_node.data)
                    if current_wavelet_tree_node.left or current_wavelet_tree_node.right:
                        node_traversal_queue.append(current_wavelet_tree_node.left)
                        node_traversal_queue.append(current_wavelet_tree_node.right)

            # Append the current level's data to the final result list representing the wavelet tree levels
            wavelet_tree_level_order_representation.append(current_level_node_data)

        # Return the level-order representation of the wavelet tree
        return wavelet_tree_level_order_representation

    # Method to count occurrences of a specific target value up to a given position in the original data array
    def rank(self, target_character_to_find, target_position_limit):
        # If the target value is outside the range of the data array values, return 0 as it cannot occur
        if (
            not self.root_node_reference
            or target_character_to_find < min(self.original_input_data_array)
            or target_character_to_find > max(self.original_input_data_array)
        ):
            return 0  # Return zero occurrences if target value is out of valid range

        # Initialize a counter to track how many times the target value has been encountered
        character_occurrence_counter = 0

        # Traverse the original data array up to the specified limit, counting occurrences of the target value
        for current_index_in_array in range(target_position_limit):
            if self.original_input_data_array[current_index_in_array] == target_character_to_find:
                character_occurrence_counter += 1  # Increment counter when the target value is encountered

        # Return the final count of occurrences of the target value up to the specified position
        return character_occurrence_counter

# Instantiate the Wavelet_Tree class with a new data array and display its level order representation
# wv_tree = Wavelet_Tree([15, 7, 20, 3, 8, 10, 12])
# print(wv_tree.get_wavelet_level_order())  # This example will show the hierarchical partitioning structure

# Test the rank function to find the number of occurrences of the number 8 up to the 5th position in the data array
# print(wv_tree.rank(8, 5))  # Expected output varies depending on data structure; could be 1 or 0 based on input


def palin_break(s: str):
    # Helper function to verify if a given substring is a palindrome by checking if it matches its reverse
    def is_palindrome(current_substring_to_evaluate: str) -> bool:
        return current_substring_to_evaluate == current_substring_to_evaluate[::-1]

    # Recursive backtracking function to explore all potential palindromic partitions of the string
    def backtrack(current_starting_index: int, current_partitioned_substrings: list):
        # If the end of the string is reached, store the current list of partitions as one possible solution
        if current_starting_index == len(s):
            all_possible_palindromic_partitions.append(
                current_partitioned_substrings[:]
            )  # Append a copy of current partition configuration
            return

        # Generate all substrings starting from the current index, evaluating each for palindromic properties
        for current_end_index in range(current_starting_index + 1, len(s) + 1):
            potential_palindromic_substring = s[current_starting_index:current_end_index]  # Extract substring
            if is_palindrome(potential_palindromic_substring):
                # If the substring is a palindrome, add it to the current partition and recursively explore further
                current_partitioned_substrings.append(potential_palindromic_substring)
                backtrack(current_end_index, current_partitioned_substrings)
                # Remove the last added substring to backtrack and explore other potential partitions
                current_partitioned_substrings.pop()

    # Initialize a list to store all palindromic partitions found during backtracking
    all_possible_palindromic_partitions = []
    backtrack(0, [])  # Begin backtracking from the start of the string
    return all_possible_palindromic_partitions

# Testing the palin_break function with a different input string to explore all palindromic partitions of "madamimadam"
# print(palin_break("madamimadam"))  # Expected output is a list of lists with various palindromic partition configurations


def heavenGates(scroll1, scroll2, scroll3):
    # Check if the combined length of scroll1 and scroll2 matches the length of scroll3; if not, return False
    if len(scroll1) + len(scroll2) != len(scroll3):
        return False  # Return False as interleaving is impossible due to mismatched lengths

    # Initialize a 2D dynamic programming table where dp[i][j] denotes interleaving possibility up to positions i and j
    interleaving_possible_table = [[False] * (len(scroll2) + 1) for _ in range(len(scroll1) + 1)]

    # Set the base case: True if both scroll1 and scroll2 are empty and match the beginning of scroll3
    interleaving_possible_table[0][0] = True

    # Populate the dynamic programming table based on characters in scroll1 and scroll2 matching with scroll3
    for scroll1_index in range(len(scroll1) + 1):
        for scroll2_index in range(len(scroll2) + 1):
            # Check if a character from scroll1 can match the next character in scroll3
            if (
                scroll1_index > 0
                and scroll1[scroll1_index - 1] == scroll3[scroll1_index + scroll2_index - 1]
            ):
                interleaving_possible_table[scroll1_index][scroll2_index] = (
                    interleaving_possible_table[scroll1_index][scroll2_index]
                    or interleaving_possible_table[scroll1_index - 1][scroll2_index]
                )

            # Check if a character from scroll2 can match the next character in scroll3
            if (
                scroll2_index > 0
                and scroll2[scroll2_index - 1] == scroll3[scroll1_index + scroll2_index - 1]
            ):
                interleaving_possible_table[scroll1_index][scroll2_index] = (
                    interleaving_possible_table[scroll1_index][scroll2_index]
                    or interleaving_possible_table[scroll1_index][scroll2_index - 1]
                )

    # Return the result in the bottom-right corner of the table, indicating if complete interleaving is possible
    return interleaving_possible_table[len(scroll1)][len(scroll2)]

# Testing heavenGates function with distinct scrolls to verify if an interleaved sequence is possible
# print(heavenGates("xyz", "uvw", "xuyvzw"))  # Expected output: True if interleaving matches scroll3
# print(heavenGates("xyz", "uvw", "xuvyz"))   # Expected output: False if interleaving is not possible


def magical_recipe(total_cases: int, binary_strings: list[str]) -> list[int]:
    MODULO_PRIME = 998244353  # Use a large prime to keep results within bounds and prevent overflow during calculations
    result_list = []  # List to store the number of ways for each binary string in the input list

    # Process each binary string case individually to calculate possible mappings
    for binary_string in binary_strings:
        string_length = len(binary_string)  # Store the length of the binary string
        # Dynamic programming array initialized with zeroes; ad[i] holds ways to map up to position i
        ways_to_map_binary_string = [0] * (string_length + 1)
        ways_to_map_binary_string[0] = 1  # Base case where an empty string has one valid mapping

        # Process each character position in the binary string, updating mapping counts for single and double characters
        for current_position in range(1, string_length + 1):
            # Handle cases where we map individual 'a' or 'b' characters
            if current_position >= 1:
                if binary_string[current_position - 1] == 'a':
                    ways_to_map_binary_string[current_position] = (
                        ways_to_map_binary_string[current_position]
                        + ways_to_map_binary_string[current_position - 1]
                    ) % MODULO_PRIME  # Mapping 'a' as '01'

                elif binary_string[current_position - 1] == 'b':
                    ways_to_map_binary_string[current_position] = (
                        ways_to_map_binary_string[current_position]
                        + ways_to_map_binary_string[current_position - 1]
                    ) % MODULO_PRIME  # Mapping 'b' as '10'

            # Handle cases where we map consecutive 'ab' or 'ba' substrings in the binary string
            if current_position >= 2:
                if binary_string[current_position - 2 : current_position] == 'ab':
                    ways_to_map_binary_string[current_position] = (
                        ways_to_map_binary_string[current_position]
                        + ways_to_map_binary_string[current_position - 2]
                    ) % MODULO_PRIME  # Mapping 'ab' as '010'

                elif binary_string[current_position - 2 : current_position] == 'ba':
                    ways_to_map_binary_string[current_position] = (
                        ways_to_map_binary_string[current_position]
                        + ways_to_map_binary_string[current_position - 2]
                    ) % MODULO_PRIME  # Mapping 'ba' as '101'

        # Append the total ways to map each string to the result list
        result_list.append(ways_to_map_binary_string[string_length])

    return result_list  # Return the list of results, one for each binary string

# Testing magical_recipe with binary strings and total cases specified
# T = 2
# cases = ["aab", "baa"]
# print(magical_recipe(T, cases))  # Expected output based on binary string mapping rules; may vary by string


import heapq  # Import heapq to manage priority queues effectively for task scheduling and order management
from collections import Counter, deque  # Import Counter for task frequency counting, deque for managing cooldowns

def lelouch_task_schedule(tasks: list[str], cooldown_interval: int) -> int:
    # Calculate how frequently each task appears in the list using Counter
    task_frequency_counter = Counter(tasks)

    # Create a max heap of task counts (using negative values since heapq is min heap by default)
    max_heap_task_counts = [-task_count for task_count in task_frequency_counter.values()]
    heapq.heapify(max_heap_task_counts)  # Convert list into a max heap

    # Queue to manage tasks currently in cooldown, holding task counts and the time they can be executed again
    cooldown_queue_tracker = deque()
    current_time_unit = 0  # Initialize a counter to track the current time in task execution units

    # Continue processing until there are no tasks left in the heap or cooldown queue
    while max_heap_task_counts or cooldown_queue_tracker:
        current_time_unit += 1  # Move forward in time as we execute tasks

        # If there are tasks available in the heap, process the most frequent task by removing it from the heap
        if max_heap_task_counts:
            current_task_count_remaining = heapq.heappop(max_heap_task_counts) + 1  # Pop from heap and increment count
            if current_task_count_remaining != 0:
                # If the task count is still greater than zero, place it in cooldown for re-scheduling later
                cooldown_queue_tracker.append((current_task_count_remaining, current_time_unit + cooldown_interval))

        # If any task's cooldown period has ended, it can be re-added to the heap for further scheduling
        if cooldown_queue_tracker and cooldown_queue_tracker[0][1] == current_time_unit:
            heapq.heappush(max_heap_task_counts, cooldown_queue_tracker.popleft()[0])  # Re-add to the heap

    # Return the total time units required to complete all tasks with specified cooldown intervals
    return current_time_unit

# Testing lelouch_task_schedule function to verify task scheduling with cooldown requirements
# tasks_example = ["X", "Y", "X", "Z", "Y", "Z"]
# cooldown_interval = 2
# print(lelouch_task_schedule(tasks_example, cooldown_interval))  # Output will vary based on input task order and cooldown


import heapq  # Import heapq for priority queue operations required to manage buy and sell orders efficiently

def rajsTradingShowdown(order_list: list[list[int]]) -> int:
    MODULO_CONSTANT = 10**9 + 7  # A large constant to ensure results remain manageable and avoid overflow
    buy_order_heap = []  # Max heap to store buy orders (negate prices to mimic max heap in Python)
    sell_order_heap = []  # Min heap for selling orders, stores minimum sell prices

    # Loop through each order and process based on whether it's a buy or sell order
    for order_price, order_amount, order_type in order_list:
        if order_type == 0:  # Handle buy orders
            # Attempt to match the buy order with the lowest price sell orders available in the sell heap
            while order_amount > 0 and sell_order_heap and sell_order_heap[0][0] <= order_price:
                current_sell_price, current_sell_amount = heapq.heappop(sell_order_heap)
                if current_sell_amount > order_amount:
                    # Partially match buy order with available sell order, pushing the remaining back to the heap
                    heapq.heappush(sell_order_heap, (current_sell_price, current_sell_amount - order_amount))
                    order_amount = 0
                else:
                    # Fully match and consume the current sell order, reducing buy order amount by this match
                    order_amount -= current_sell_amount

            # If there's still a remaining amount in the buy order, add it to the buy heap for future matching
            if order_amount > 0:
                heapq.heappush(buy_order_heap, (-order_price, order_amount))

        else:  # Handle sell orders
            # Attempt to match the sell order with the highest price buy orders available in the buy heap
            while order_amount > 0 and buy_order_heap and -buy_order_heap[0][0] >= order_price:
                current_buy_price, current_buy_amount = heapq.heappop(buy_order_heap)
                if current_buy_amount > order_amount:
                    # Partially match sell order with available buy order, pushing remaining back to the buy heap
                    heapq.heappush(buy_order_heap, (current_buy_price, current_buy_amount - order_amount))
                    order_amount = 0
                else:
                    # Fully match and consume the current buy order, reducing sell order amount by this match
                    order_amount -= current_buy_amount

            # If there's still a remaining amount in the sell order, add it to the sell heap for future matching
            if order_amount > 0:
                heapq.heappush(sell_order_heap, (order_price, order_amount))

    # Calculate the total remaining orders that could not be matched and return this count modulo the constant
    total_remaining_orders = sum(amount for _, amount in buy_order_heap) + sum(amount for _, amount in sell_order_heap)
    return total_remaining_orders % MODULO_CONSTANT

# Testing rajsTradingShowdown with distinct order lists to observe how unmatched orders accumulate
# order_example = [[8, 7, 0], [12, 3, 1], [18, 2, 1], [14, 5, 0]]
# print(rajsTradingShowdown(order_example))  # Result varies based on order matches, indicating remaining unmatched orders


from collections import deque  # Import deque to facilitate BFS for shortest path in grid traversal

def collect_items(matrix_grid: list[list[int]]) -> int:
    # Get the dimensions of the input grid where items are located
    total_rows, total_columns = len(matrix_grid), len(matrix_grid[0])

    # Identify and sort all items in the grid with values greater than 1; keep track of their positions
    items_to_collect = sorted(
        [
            (matrix_grid[row][col], row, col)
            for row in range(total_rows)
            for col in range(total_columns)
            if matrix_grid[row][col] > 1
        ]
    )
    # Insert the starting position at (1, 0, 0) since it's the entry point of the grid
    items_to_collect.insert(0, (1, 0, 0))

    # Helper function to execute BFS and calculate the shortest path between two points
    def bfs_shortest_path(start_row, start_column, target_row, target_column):
        # Track visited grid positions to avoid revisits and redundant calculations
        visited_positions = [[False] * total_columns for _ in range(total_rows)]
        # Queue initialization with the starting position and a counter for steps taken
        bfs_queue = deque([(start_row, start_column, 0)])
        visited_positions[start_row][start_column] = True  # Mark start as visited

        # Process each position in the BFS queue to find the shortest path to the target location
        while bfs_queue:
            current_row, current_column, steps_taken = bfs_queue.popleft()
            # If the target position is reached, return the accumulated number of steps
            if current_row == target_row and current_column == target_column:
                return steps_taken

            # Explore all four potential movement directions and enqueue valid moves
            for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_column = current_row + row_offset, current_column + col_offset
                if (
                    0 <= new_row < total_rows
                    and 0 <= new_column < total_columns
                    and not visited_positions[new_row][new_column]
                    and matrix_grid[new_row][new_column] != 0
                ):
                    visited_positions[new_row][new_column] = True  # Mark new position as visited
                    bfs_queue.append((new_row, new_column, steps_taken + 1))  # Increment steps

        # Return -1 if the target is unreachable from the starting position
        return -1

    # Initialize a counter for the total steps required to collect all items in sorted order
    total_steps_to_collect_items = 0

    # Iterate over each pair of consecutive items, calculating the shortest path between them
    for item_index in range(1, len(items_to_collect)):
        _, start_row, start_column = items_to_collect[item_index - 1]
        _, target_row, target_column = items_to_collect[item_index]

        # Use BFS to calculate the shortest distance between the current item and the next
        steps_to_next_item = bfs_shortest_path(start_row, start_column, target_row, target_column)
        if steps_to_next_item == -1:
            return -1  # If any item is unreachable, return -1 to indicate an incomplete path

        # Accumulate steps to the total count as items are collected in sequence
        total_steps_to_collect_items += steps_to_next_item

    # Return the overall total of steps needed to collect all items in the grid
    return total_steps_to_collect_items

# Testing collect_items with a specific matrix layout to calculate minimal steps for item collection
# matrix_example = [[1, 0, 4], [0, 5, 3], [2, 6, 0]]
# print(collect_items(matrix_example))  # Expected output is the shortest path steps or -1 if some items are unreachable


from collections import Counter  # Import Counter to simplify character frequency counting in the string

def frequencySort(input_string: str) -> str:
    # Count how often each character appears in the input string
    character_frequency_counter = Counter(input_string)

    # Sort characters by descending frequency, and within the same frequency, sort by ASCII ascending order
    sorted_characters_by_frequency = sorted(
        character_frequency_counter.items(), key=lambda item: (-item[1], item[0])
    )

    # Construct the result string by repeating each character according to its frequency
    sorted_frequency_string = ''.join(character * frequency for character, frequency in sorted_characters_by_frequency)

    # Return the final string with characters ordered by frequency
    return sorted_frequency_string

# Testing frequencySort with a string input to reorder characters based on frequency in descending order
# example_string = "mississippi"
# print(frequencySort(example_string))  # Expected output is "ssssiiippm" or similar with high-frequency characters first


from typing import List, Tuple  # Import List and Tuple for precise type annotations

def min_rooms_required(arrival_departure_times: List[Tuple[int, int]]) -> int:
    # Separate and sort arrival times and departure times into two individual lists
    sorted_arrival_times = sorted([arrival for arrival, departure in arrival_departure_times])
    sorted_departure_times = sorted([departure for arrival, departure in arrival_departure_times])

    # Initialize room usage counters: current rooms in use and maximum rooms required so far
    current_rooms_in_use = 0
    maximum_rooms_needed = 0
    arrival_pointer, departure_pointer = 0, 0  # Pointers to navigate the sorted lists

    # Traverse both lists using two pointers, comparing arrivals and departures to determine room allocation
    while arrival_pointer < len(sorted_arrival_times):
        # If the next guest arrives before the previous one departs, increment room count
        if sorted_arrival_times[arrival_pointer] <= sorted_departure_times[departure_pointer]:
            current_rooms_in_use += 1  # Allocate a new room
            maximum_rooms_needed = max(maximum_rooms_needed, current_rooms_in_use)  # Update max rooms if needed
            arrival_pointer += 1
        else:
            # If a guest departs, free up a room by decrementing the room count in use
            current_rooms_in_use -= 1
            departure_pointer += 1

    # Return the maximum number of rooms required to accommodate all guests with the given schedule
    return maximum_rooms_needed

# Testing min_rooms_required function to determine the minimum number of rooms needed for a schedule
# example_arrival_departure_times = [(1, 3), (2, 6), (8, 10), (5, 9)]
# print(min_rooms_required(example_arrival_departure_times))  # Expected output is the maximum room count required


import heapq  # Import heapq to create priority queues for Huffman encoding efficiently
from collections import Counter  # Import Counter for calculating character frequencies in Huffman encoding

# Define the Huffman class, which implements encoding and decoding based on character frequency
class Huffman:
    def __init__(self):
        self.huffman_codes = {}  # Dictionary to store generated Huffman codes for each character
        self.source_string_to_encode = ""  # Variable to hold the source string that will be encoded

    # Method to set the source string and prepare it for Huffman encoding
    def set_source_string(self, src_str: str):
        self.source_string_to_encode = src_str  # Assign the input string to the class attribute

    # Method to generate Huffman codes for each character in the source string
    def generate_codes(self):
        self.huffman_codes = {}  # Reset any previously stored codes

        # Count character frequencies using Counter, creating a list of [frequency, character] pairs
        character_frequency_counter = Counter(self.source_string_to_encode)
        frequency_heap = [[character_frequency_counter[character], character] for character in character_frequency_counter]
        heapq.heapify(frequency_heap)  # Transform the list into a min-heap for efficient extraction

        # Build the Huffman tree by combining nodes with the lowest frequencies iteratively
        while len(frequency_heap) > 1:
            lowest_frequency_node = heapq.heappop(frequency_heap)  # Extract the two nodes with the lowest frequency
            second_lowest_frequency_node = heapq.heappop(frequency_heap)

            # Assign '0' and '1' to each character path in the lowest nodes
            for character in lowest_frequency_node[1:]:
                self.huffman_codes[character] = '0' + self.huffman_codes.get(character, '')
            for character in second_lowest_frequency_node[1:]:
                self.huffman_codes[character] = '1' + self.huffman_codes.get(character, '')

            # Merge the nodes and push the combined frequency back into the heap
            combined_frequency_node = [lowest_frequency_node[0] + second_lowest_frequency_node[0]] + \
                                      lowest_frequency_node[1:] + second_lowest_frequency_node[1:]
            heapq.heappush(frequency_heap, combined_frequency_node)

    # Method to encode a string based on generated Huffman codes
    def encode_message(self, message_to_encode: str) -> str:
        if not self.huffman_codes:
            raise ValueError("Huffman codes have not been generated. Call generate_codes() first.")
        return ''.join(self.huffman_codes[char] for char in message_to_encode)  # Encode by mapping each char

    # Method to decode an encoded Huffman message back to its original text
    def decode_message(self, encoded_msg: str) -> str:
        if not self.huffman_codes:
            raise ValueError("Huffman codes have not been generated. Call generate_codes() first.")

        reverse_huffman_codes = {code: char for char, code in self.huffman_codes.items()}  # Reverse map codes
        decoded_message, current_code = "", ""  # Initialize decoded message and temporary code accumulator

        # Iterate through bits in encoded message, matching accumulated bits to characters
        for bit in encoded_msg:
            current_code += bit
            if current_code in reverse_huffman_codes:
                decoded_message += reverse_huffman_codes[current_code]
                current_code = ""  # Reset code for next character

        return decoded_message  # Return the fully decoded message

# Testing Huffman encoding and decoding with a unique source string to verify encoding correctness
# huffman = Huffman()
# huffman.set_source_string("banana")
# huffman.generate_codes()
# print(huffman.huffman_codes)  # Expected output: Huffman codes for characters in "banana"
# encoded_message = huffman.encode_message("ban")
# print(encoded_message)  # Encoded output based on Huffman codes
# print(huffman.decode_message(encoded_message))  # Should output the original "ban" string after decoding