# Class representing a store in the binary tree
class Store:
    # Initialize a store with an id and pointers to left and right children
    def __init__(self, store_id, left_child=None, right_child=None):
        self.id = store_id  # Store the ID of the store
        self.left = left_child  # Pointer to the left child store
        self.right = right_child  # Pointer to the right child store

# Function to find the nearest common facility (LCA) for two store IDs
def find_nearest_common_facility(tree_root, target_store_id1, target_store_id2):
    # Base case: If the root is None, return None
    if not tree_root:
        return None
    
    # If the current node is one of the target store IDs, return its ID
    if tree_root.id == target_store_id1 or tree_root.id == target_store_id2:
        return tree_root.id
    
    # Recur for the left and right subtrees
    left_lca = find_nearest_common_facility(tree_root.left, target_store_id1, target_store_id2)  # Search in left subtree
    right_lca = find_nearest_common_facility(tree_root.right, target_store_id1, target_store_id2)  # Search in right subtree
    
    # If both left and right LCA are found, the current node is the LCA
    if left_lca and right_lca:
        return tree_root.id  # Return the current node's ID as LCA
    
    # Return the non-None result from either left or right subtree
    return left_lca if left_lca else right_lca

# Function to test and print the nearest common facility
def test_find_nearest_common_facility(tree_root, target_store_id1, target_store_id2):
    # Call the function to find LCA
    lca_id = find_nearest_common_facility(tree_root, target_store_id1, target_store_id2)
    
    # If LCA is found, print the result
    if lca_id:
        print(f"LCA of {target_store_id1} and {target_store_id2} is: {lca_id}")
    else:
        print(f"LCA of {target_store_id1} and {target_store_id2} not found.")

# Building the test binary tree
'''
    Tree Structure:
          3
         / \
        5   1
       / \
      6   2
         / \
        7   4
'''
# # Create the root store node
# root_store = Store(3)  
# # Assign left and right children
# root_store.left = Store(5)  
# root_store.right = Store(1)  
# root_store.left.left = Store(6)  
# root_store.left.right = Store(2)  
# root_store.left.right.left = Store(7)  
# root_store.left.right.right = Store(4)  

# # Test Case 1: Find LCA of store IDs 5 and 1
# test_find_nearest_common_facility(root_store, 5, 1)  # Expected Output: 3

# # Test Case 2: Find LCA of store IDs 5 and 4
# test_find_nearest_common_facility(root_store, 5, 4)  # Expected Output: 5

# # Test Case 3: Find LCA of store IDs 6 and 4
# test_find_nearest_common_facility(root_store, 6, 4)  # Expected Output: 5

# # Test Case 4: Find LCA of store IDs 7 and 4
# test_find_nearest_common_facility(root_store, 7, 4)  # Expected Output: 2