from collections import deque  # Import deque for efficient queue operations

def arrangePerformers(nums):
    # Sort the numbers in descending order
    nums.sort(reverse=True)  
    # Initialize an empty deque to store the arrangement
    queue = deque()          
    
    # Iterate through each number in the sorted list
    for i in nums:           
        # If the queue is not empty
        if queue:            
            # Move the last element to the front
            queue.appendleft(queue.pop())  
        # Add the current number to the front of the queue
        queue.appendleft(i)  

    # Convert the deque back to a list and return it
    return list(queue)       

# Example usage
# Uncomment to test
# print(arrangePerformers([17, 13, 11, 2, 3, 5, 7]))  
