from collections import deque

class NodeWithBuddies:
    def __init__(self, value, left_child=None, right_child=None, next_node=None, prev_node=None):
        # Initialize the node with its value and pointers to left, right, next, and previous nodes
        self.val = value
        self.left = left_child
        self.right = right_child
        self.next = next_node
        self.prev = prev_node

def findBuddies(root: NodeWithBuddies) -> None:
    # Base case: return if the root is None
    if not root:
        return
    
    # Initialize a queue to perform level-order traversal
    queue = deque([root])
    
    # Loop until there are no more nodes in the queue
    while queue:
        level_size = len(queue)  # Get the number of nodes at the current level
        previous_node = None  # Initialize the previous node as None
        
        # Use a while loop to process all nodes at the current level
        index = 0  # Initialize index for nodes in the current level
        while index < level_size:
            new_node = queue.popleft()  # Dequeue the front node
            
            # Connect the previous node's next to the current node and vice versa
            if previous_node:
                previous_node.next = new_node  # Set the next pointer of the previous node
                new_node.prev = previous_node  # Set the previous pointer of the current node
            
            # Update previous_node to the current node
            previous_node = new_node
            
            # Enqueue the left and right children of the current node
            if new_node.left:
                queue.append(new_node.left)
            if new_node.right:
                queue.append(new_node.right)
                
            index += 1  # Increment index to process the next node

# Example usage
# root = NodeWithBuddies(1)
# root.left = NodeWithBuddies(2)
# root.right = NodeWithBuddies(3)
# findBuddies(root)
