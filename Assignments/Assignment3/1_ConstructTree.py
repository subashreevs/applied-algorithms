from collections import deque

# Class representing a node in the binary tree
class TreeNode:
    # Initialize a tree node with a value and pointers to left and right children
    def __init__(self, node_value=0, left_child=None, right_child=None):
        self.val = node_value  # Store the value of the node
        self.left = left_child  # Pointer to the left child
        self.right = right_child  # Pointer to the right child

# Function to construct a binary tree from inorder and postorder traversals
def construct_tree(inorder_values, postorder_values):
    # A map to quickly find the index of a value in the inorder list
    inorder_index_map = {}
    index = 0  # Initialize index for enumerating inorder_values
    while index < len(inorder_values):  # Iterate through inorder_values using while loop
        value = inorder_values[index]  # Get the current value
        inorder_index_map[value] = index  # Map value to its index
        index += 1  # Increment the index

    # Recursive function to build the tree
    def build_tree(left_inorder_index, right_inorder_index):
        # Base case: no elements to construct the tree
        if left_inorder_index > right_inorder_index:
            return None
        
        # The current root is the last element in postorder
        root_value = postorder_values.pop()  # Remove the last element from postorder
        root_node = TreeNode(root_value)  # Create a new TreeNode with root_value
        
        # Find the index of the root in inorder to split into left and right subtrees
        root_index = inorder_index_map[root_value]  # Get the root's index in inorder
        
        # Build the right subtree first (because of postorder traversal)
        root_node.right = build_tree(root_index + 1, right_inorder_index)  # Construct right subtree
        # Build the left subtree
        root_node.left = build_tree(left_inorder_index, root_index - 1)  # Construct left subtree
        
        return root_node  # Return the constructed subtree
    
    # Start building the tree from the full range of the inorder list
    return build_tree(0, len(inorder_values) - 1)

# Example usage (uncomment to test)
# inorder_values = [9, 3, 15, 20, 7]
# postorder_values = [9, 15, 7, 20, 3]
# root_node = construct_tree(inorder_values, postorder_values)

# Function to convert a binary tree to a list representation
def tree_to_list(tree_root):
    # If the root is None, return an empty list
    if not tree_root:
        return []
    
    level_order_values = []  # List to store the values in level order
    node_queue = deque([tree_root])  # Initialize a queue with the root node
    
    # While there are nodes in the queue
    while node_queue:
        current_node = node_queue.popleft()  # Dequeue the front node
        
        # If the current node is not None
        if current_node:
            level_order_values.append(current_node.val)  # Append its value to the result list
            node_queue.append(current_node.left)  # Enqueue the left child
            node_queue.append(current_node.right)  # Enqueue the right child
        else:
            level_order_values.append(None)  # Append None for missing nodes
    
    # Remove trailing None values that do not represent meaningful tree nodes
    while level_order_values and level_order_values[-1] is None:
        level_order_values.pop()  # Remove the last element if it's None
    
    return level_order_values  # Return the list representation of the tree

# Example usage (uncomment to test)
# inorder_values = [9, 3, 15, 20, 7]
# postorder_values = [9, 15, 7, 20, 3]
# root_node = construct_tree(inorder_values, postorder_values)
# output_list = tree_to_list(root_node)
# print(output_list)
