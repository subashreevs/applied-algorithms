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




def beautifulNinjaFormation(n: int) -> list[int]:
    # Base cases: return specific formations for n = 1 and n = 2
    if n == 1:
        return [1]  # Only one ninja, formation is [1]
    elif n == 2:
        return [1, 2]  # Two ninjas, formation is [1, 2]

    # Recursively generate beautiful ninja formation for odds and evens
    # Recursion ensures that no ninja satisfies 2 * nums[k] = nums[i] + nums[j]
    odd_count = (n + 1) // 2  # Count of odd-indexed elements
    even_count = n // 2       # Count of even-indexed elements
    
    # Generate odd-indexed elements
    odd_ninjas = beautifulNinjaFormation(odd_count)  # Odd-indexed elements
    # Generate even-indexed elements
    even_ninjas = beautifulNinjaFormation(even_count)  # Even-indexed elements

    # Initialize the result list
    result = []
    
    # Add the scaled odd ninjas to the result using a while loop
    index = 0  # Initialize the index for odd ninjas
    while index < len(odd_ninjas):
        result.append(2 * odd_ninjas[index] - 1)  # Scale and append odd ninja
        index += 1  # Move to the next odd ninja

    # Add the scaled even ninjas to the result using a while loop
    index = 0  # Initialize the index for even ninjas
    while index < len(even_ninjas):
        result.append(2 * even_ninjas[index])  # Scale and append even ninja
        index += 1  # Move to the next even ninja

    return result

# Test cases
# print(beautifulNinjaFormation(4))  # Example output: [1, 3, 2, 4]
# print(beautifulNinjaFormation(5))  # Example output: [1, 5, 3, 2, 4]



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




def endgameScores(points: list[int]) -> bool:
    # Get the number of points (games)
    num_points = len(points)

    # Create a 2D DP array initialized to 0
    dp_table = [[0] * num_points for _ in range(num_points)]
    
    # Base case: when there's only one game available
    index = 0
    while index < num_points:
        dp_table[index][index] = points[index]  # Initialize the diagonal
        index += 1

    # Fill the DP table for all possible lengths of subarrays
    length = 2  # Start with a length of 2
    while length <= num_points:  # Length of the subarray
        starting_index = 0  # Initialize starting index of the subarray
        while starting_index <= num_points - length:  # Loop to find all subarrays of current length
            ending_index = starting_index + length - 1  # Calculate the ending index
            
            # Calculate the score difference for current subarray
            dp_table[starting_index][ending_index] = max(
                points[starting_index] - dp_table[starting_index + 1][ending_index],  # Pick the start
                points[ending_index] - dp_table[starting_index][ending_index - 1]     # Pick the end
            )
            
            starting_index += 1  # Move to the next starting index
        
        length += 1  # Move to the next length of subarrays
    
    # Ronaldo wins or ties if the score difference is non-negative
    return dp_table[0][num_points - 1] >= 0

# Test Cases
# print(endgameScores([3, 99, 155, 8]))  # Output: True
# print(endgameScores([5, 1, 100, 1, 5]))  # Output: False



def satisfyingOrders(total_people: int, satisfied_people: int) -> int:
    MOD = 10**9 + 7  # Define the modulus for calculations

    # Create a DP table with (total_people + 1) x (satisfied_people + 1)
    dp_table = [[0] * (satisfied_people + 1) for _ in range(total_people + 1)]
    
    # Base case: One person can satisfy themselves
    dp_table[1][1] = 1  

    # Fill the DP table
    current_people = 2  # Start from 2 people
    while current_people <= total_people:  # Loop for the number of people
        current_satisfied = 1  # Start with 1 satisfied person
        while current_satisfied <= satisfied_people:  # Loop for the number of satisfied people
            # If the new person is satisfied
            dp_table[current_people][current_satisfied] = dp_table[current_people - 1][current_satisfied - 1]  # Last person satisfied
            
            # If the new person is not satisfied
            dp_table[current_people][current_satisfied] += (current_people - 1) * dp_table[current_people - 1][current_satisfied]
            dp_table[current_people][current_satisfied] %= MOD
            
            current_satisfied += 1  # Move to the next number of satisfied people
        
        current_people += 1  # Move to the next number of people

    return dp_table[total_people][satisfied_people]  # Return the result for total_people and satisfied_people

# Test Cases
# print(satisfyingOrders(4, 3))  # Output: 6
# print(satisfyingOrders(5, 2))  # Example case for testing



def batmanSignal(length: int):
    result_list = []  # Initialize a list to store the results

    def backtrack(current_signal):
        # Check if the current signal length equals the desired length
        if len(current_signal) == length:
            result_list.append(current_signal)  # Add the current signal to results
            return
        
        # If the current signal is empty or ends with 'x', we can add 'y'
        if not current_signal or current_signal[-1] == 'x':
            backtrack(current_signal + 'y')  # Add 'y' to the current signal
        
        # If the current signal is empty or ends with 'y' or 'x', we can add 'x'
        if not current_signal or current_signal[-1] == 'y' or current_signal[-1] == 'x':
            backtrack(current_signal + 'x')  # Add 'x' to the current signal

    backtrack("")  # Start backtracking with an empty signal
    
    return result_list  # Return the list of results

# Test Cases
# print(batmanSignal(3))  # Output: ['yxy', 'yxx', 'xyx', 'xxy', 'xxx']
# print(batmanSignal(1))  # Output: ['x', 'y']





def sacred_sequence(keys: int, position: int) -> str:
    from math import factorial
    
    # Create a list of numbers from 1 to keys
    numbers = list(range(1, keys + 1))
    
    # Adjust position for 0-based index
    k = position - 1
    
    result = []
    
    # Build the k-th permutation
    for i in range(keys, 0, -1):
        # Determine the factorial of the current number of remaining elements
        fact = factorial(i - 1)
        
        # Determine the index of the current number to use
        index = k // fact
        
        # Append the chosen number to the result
        result.append(str(numbers[index]))
        
        # Remove the used number from the list
        numbers.pop(index)
        
        # Reduce k for the next position
        k %= fact
    
    return ''.join(result)

# Test Cases
# print(sacred_sequence(3, 3))  # Output: "213"
# print(sacred_sequence(4, 9))  # Output: "2314"




class ListNode:
    def __init__(self, value=0, next_node=None):
        # Initialize the ListNode with a value and a pointer to the next node
        self.val = value
        self.next = next_node

def removeElements(head_node: ListNode, target_value: int) -> ListNode:
    # Base case: if the head_node is None, return None
    if not head_node:
        return None
    
    # Recursive call for the next node
    head_node.next = removeElements(head_node.next, target_value)
    
    # Check the current node's value
    if head_node.val == target_value:
        # Skip this node
        return head_node.next
    else:
        # Keep this node
        return head_node

# Helper function to create a linked list from a list of values
def create_linked_list(value_list):
    # If the input list is empty, return None
    if not value_list:
        return None
    # Initialize the head node of the linked list
    head_node = ListNode(value_list[0])
    current_node = head_node  # Pointer to the current node
    index = 1  # Index for traversing the value_list
    
    # Use a while loop to create the linked list
    while index < len(value_list):
        # Create a new ListNode for the next value
        current_node.next = ListNode(value_list[index])
        current_node = current_node.next  # Move to the next node
        index += 1  # Increment index to process the next value
    
    return head_node  # Return the head of the linked list

# Helper function to convert linked list to a list for easy display
def linked_list_to_list(head_node):
    result_list = []  # Initialize an empty list to store values
    current_node = head_node  # Pointer to traverse the linked list
    
    # Use a while loop to traverse the linked list
    while current_node:
        result_list.append(current_node.val)  # Append the current node's value to result_list
        current_node = current_node.next  # Move to the next node
    
    return result_list  # Return the resulting list

# Example usage
# head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
# new_head = removeElements(head, 6)
# print(linked_list_to_list(new_head))  # Output: [1, 2, 3, 4, 5]

# empty_head = create_linked_list([])
# new_empty_head = removeElements(empty_head, 1)
# print(linked_list_to_list(new_empty_head))  # Output: []

# head2 = create_linked_list([7, 7, 7, 7])
# new_head2 = removeElements(head2, 7)
# print(linked_list_to_list(new_head2))  # Output: []



def rearrangeAllToys(toy_list):
    # Sort the toys array
    toy_list.sort()
    total_toys = len(toy_list)
    
    # Create a new array to store the rearranged toys
    rearranged_toys = [0] * total_toys
    
    # Find the middle index and set up two pointers
    middle_index = (total_toys + 1) // 2
    left_pointer = middle_index - 1  # Pointer for smaller elements
    right_pointer = total_toys - 1     # Pointer for larger elements
    
    # Use a while loop to fill the rearranged array in a zig-zag pattern
    index = 0  # Initialize index for the rearranged array
    while index < total_toys:
        if index % 2 == 0:
            # Even index: take from the left (smaller elements)
            rearranged_toys[index] = toy_list[left_pointer]
            left_pointer -= 1  # Move left pointer to the left
        else:
            # Odd index: take from the right (larger elements)
            rearranged_toys[index] = toy_list[right_pointer]
            right_pointer -= 1  # Move right pointer to the left
        
        index += 1  # Increment index to move to the next position
    
    return rearranged_toys

# Example usage
# toys1 = [1, 5, 1, 1, 6, 4]
# print(rearrangeAllToys(toys1))  # Output: [1, 6, 1, 5, 1, 4]

# toys2 = [1, 3, 2, 2, 3, 1]
# print(rearrangeAllToys(toys2))  # Output: [2, 3, 1, 3, 1, 2]



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





