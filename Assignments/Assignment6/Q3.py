def findMaxLength(nums: list[int]) -> int:
    prefix_map = {}  # Stores the first occurrence of each prefix sum
    prefix_sum = 0
    max_length = 0
    
    for i, num in enumerate(nums):
        # Update prefix sum
        prefix_sum += 1 if num == 1 else -1
        
        if prefix_sum == 0:
            # If the sum is zero, the subarray from 0 to i is balanced
            max_length = i + 1
        elif prefix_sum in prefix_map:
            # If the prefix_sum was seen before, calculate the subarray length
            max_length = max(max_length, i - prefix_map[prefix_sum])
        else:
            # Store the first occurrence of the prefix_sum
            prefix_map[prefix_sum] = i
    
    return max_length


# Test Case 1: Simple balanced subarray
nums = [0, 1]
print("Test Case 1 Output:", findMaxLength(nums))  # Expected Output: 2

# Test Case 2: Multiple balanced segments
nums = [0, 1, 0]
print("Test Case 2 Output:", findMaxLength(nums))  # Expected Output: 2
