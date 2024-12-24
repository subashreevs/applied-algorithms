from collections import deque  # Import deque for efficient queue operations in BFS

def collect_items(matrix_grid: list[list[int]]) -> int:
    # Get the dimensions of the matrix grid
    total_rows, total_columns = len(matrix_grid), len(matrix_grid[0])

    # Collect all items in the grid that are greater than 1, along with their positions, and sort them
    items_to_collect = sorted([(matrix_grid[row][col], row, col) 
                               for row in range(total_rows) 
                               for col in range(total_columns) 
                               if matrix_grid[row][col] > 1])
    # Add the starting position at (1, 0, 0) where 1 represents the starting item
    items_to_collect.insert(0, (1, 0, 0))

    # Helper function to perform BFS and find shortest path between two points
    def bfs_shortest_path(start_row, start_column, target_row, target_column):
        # Track visited positions within the grid
        visited_positions = [[False] * total_columns for _ in range(total_rows)]
        # Initialize queue with starting position and zero steps taken
        bfs_queue = deque([(start_row, start_column, 0)])
        visited_positions[start_row][start_column] = True  # Mark start as visited

        # Process each position in the queue
        while bfs_queue:
            current_row, current_column, steps_taken = bfs_queue.popleft()
            # If the target position is reached, return the number of steps taken
            if current_row == target_row and current_column == target_column:
                return steps_taken
            
            # Check all four directions for possible moves
            for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_column = current_row + row_offset, current_column + col_offset
                # Ensure the new position is within bounds, not visited, and not blocked
                if 0 <= new_row < total_rows and 0 <= new_column < total_columns and \
                   not visited_positions[new_row][new_column] and matrix_grid[new_row][new_column] != 0:
                    visited_positions[new_row][new_column] = True  # Mark new position as visited
                    bfs_queue.append((new_row, new_column, steps_taken + 1))  # Add new position to queue with incremented steps
        
        return -1  # Return -1 if target is unreachable

    # Initialize total steps to collect all items
    total_steps_to_collect_items = 0

    # Iterate over all items to collect, calculating shortest path between consecutive items
    for item_index in range(1, len(items_to_collect)):
        _, start_row, start_column = items_to_collect[item_index - 1]
        _, target_row, target_column = items_to_collect[item_index]
        
        # Use BFS to calculate steps required to reach the next item
        steps_to_next_item = bfs_shortest_path(start_row, start_column, target_row, target_column)
        if steps_to_next_item == -1:
            return -1  # Return -1 if an item is unreachable
        
        # Accumulate the steps taken
        total_steps_to_collect_items += steps_to_next_item

    # Return the total steps required to collect all items in sorted order
    return total_steps_to_collect_items

# # Example usage
# matrix_example_1 = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
# print(collect_items(matrix_example_1))  # Expected output: 6

# matrix_example_2 = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]
# print(collect_items(matrix_example_2))  # Expected output: -1
