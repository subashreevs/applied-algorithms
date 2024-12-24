def longestUniformSegment(boxes: str, changes: int) -> int:
    def max_length_with_target(target):
        left = 0
        max_length = 0
        change_count = 0
        
        for right in range(len(boxes)):
            # Increment change_count if the current box is not the target
            if boxes[right] != target:
                change_count += 1
            
            # If change_count exceeds allowed changes, shrink the window
            while change_count > changes:
                if boxes[left] != target:
                    change_count -= 1
                left += 1
            
            # Calculate the current window length
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    # Check for each unique character in the string
    unique_chars = set(boxes)
    longest_segment = 0
    
    for char in unique_chars:
        longest_segment = max(longest_segment, max_length_with_target(char))
    
    return longest_segment

# Test cases
print(longestUniformSegment("aabbcc", 6))  # Output: 6
print(longestUniformSegment("abcbbab", 2))  # Output: 6