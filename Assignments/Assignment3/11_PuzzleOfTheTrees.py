from collections import defaultdict, deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def puzzleOfTheTrees(root: TreeNode) -> List[List[int]]:
    # If the root is None, return an empty list
    if not root:
        return []

    # This will hold the nodes at each column
    column_table = defaultdict(list)
    
    # Queue for BFS; store tuples of (node, column_index, depth)
    bfs_queue = deque([(root, 0, 0)])  # (node, column_index, depth)
    
    # Continue until there are no more nodes to process in the queue
    while bfs_queue:
        current_node, column_index, current_depth = bfs_queue.popleft()
        
        # Append the current node's value and its depth to the column table
        column_table[column_index].append((current_depth, current_node.val))
        
        # If the current node has a left child, add it to the queue
        if current_node.left:
            bfs_queue.append((current_node.left, column_index - 1, current_depth + 1))
        
        # If the current node has a right child, add it to the queue
        if current_node.right:
            bfs_queue.append((current_node.right, column_index + 1, current_depth + 1))

    # Sort the columns by their index
    sorted_column_indices = sorted(column_table.keys())
    result = []
    
    # Iterate over each sorted column index
    index = 0
    while index < len(sorted_column_indices):
        column_key = sorted_column_indices[index]
        
        # Sort the entries in the column by depth, then by node value
        sorted_column_nodes = sorted(column_table[column_key], key=lambda x: (x[0], x[1]))
        
        # Append the sorted values to the result list
        result.append([val for _, val in sorted_column_nodes])
        
        index += 1  # Move to the next column index
    
    return result

# Example usage:
# Construct the tree from the first example
# root1 = TreeNode(3)
# root1.left = TreeNode(9)
# root1.right = TreeNode(20)
# root1.right.left = TreeNode(15)
# root1.right.right = TreeNode(7)

# print(puzzleOfTheTrees(root1))  # Output: [[9],[3,15],[20],[7]]

# Construct the tree from the second example
# root2 = TreeNode(1)
# root2.left = TreeNode(2)
# root2.right = TreeNode(3)
# root2.left.left = TreeNode(4)
# root2.left.right = TreeNode(6)
# root2.right.left = TreeNode(5)
# root2.right.right = TreeNode(7)

# print(puzzleOfTheTrees(root2))  # Output: [[4],[2],[1,5,6],[3],[7]]

# Construct the tree from the third example
# root3 = TreeNode(1)
# root3.left = TreeNode(2)
# root3.right = TreeNode(3)
# root3.left.left = TreeNode(4)
# root3.left.right = TreeNode(5)
# root3.right.left = TreeNode(6)
# root3.right.right = TreeNode(7)

# print(puzzleOfTheTrees(root3))  # Output: [[4],[2],[1,5,6],[3],[7]]
