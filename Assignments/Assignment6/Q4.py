from typing import List, Tuple

def breaches(levels: List[int]) -> List[Tuple[int, int]]:
    prefix_map = {}  # Maps prefix_sum to the list of indices where it occurs
    prefix_sum = 0
    result = []
    
    for i, num in enumerate(levels):
        prefix_sum += num
        
        # Check if prefix_sum is zero (subarray from start to current index)
        if prefix_sum == 0:
            result.append((0, i))
        
        # If prefix_sum is already seen, there are zero-sum subarrays
        if prefix_sum in prefix_map:
            for start_index in prefix_map[prefix_sum]:
                result.append((start_index + 1, i))
        
        # Add the current prefix_sum and its index to the map
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = []
        prefix_map[prefix_sum].append(i)
    
    return result


# Test Case 1
levels = [3, 4, -7, 1, 2, -6, 4, -1]
print("Test Case 1 Output:", breaches(levels))  
# Expected Output: [(0, 2), (1, 4), (4, 6), (0, 7), (3, 7)]

# Test Case 2
levels = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
print("Test Case 2 Output:", breaches(levels))  
# Expected Output: [(2, 4), (2, 6), (5, 6), (6, 9), (0, 10)]