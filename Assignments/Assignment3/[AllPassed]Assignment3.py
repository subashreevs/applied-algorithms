from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(inorder, postorder):
    # A map to quickly find the index of a value in the inorder list
    inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
    
    # Recursive function to build the tree
    def build_tree(left_inorder, right_inorder):
        # Base case: no elements to construct the tree
        if left_inorder > right_inorder:
            return None
        
        # The current root is the last element in postorder
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder to split into left and right subtrees
        index = inorder_index_map[root_val]
        
        # Build the right subtree first (because of postorder traversal)
        root.right = build_tree(index + 1, right_inorder)
        root.left = build_tree(left_inorder, index - 1)
        
        return root
    
    # Start building the tree from the full range of inorder list
    return build_tree(0, len(inorder) - 1)

# Example usage
# inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]
# root = construct_tree(inorder, postorder)


# def tree_to_list(root):
#     if not root:
#         return []
    
#     result = []
#     queue = deque([root])
    
#     while queue:
#         node = queue.popleft()
        
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
    
#     # Remove trailing 'None' values that don't represent meaningful tree nodes
#     while result and result[-1] is None:
#         result.pop()
    
#     return result

# # Example usage
# inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]
# root = construct_tree(inorder, postorder)
# output = tree_to_list(root)
# print(output)



class Store:
    def __init__(self, id, left=None, right=None):
        self.id = id
        self.left = left
        self.right = right

def find_nearest_common_facility(root, storeId1, storeId2):
    # Base case: If root is None or if we find either storeId1 or storeId2, return root
    if not root:
        return None
    if root.id == storeId1 or root.id == storeId2:
        return root.id
    
    # Recur for the left and right subtrees
    left_lca = find_nearest_common_facility(root.left, storeId1, storeId2)
    right_lca = find_nearest_common_facility(root.right, storeId1, storeId2)
    
    # If both the left and right subtrees return non-None values, current root is the LCA
    if left_lca and right_lca:
        return root.id
    
    # Otherwise, return the non-None result from either subtree
    return left_lca if left_lca else right_lca

# Function to help test and print LCA
# def test_find_nearest_common_facility(root, storeId1, storeId2):
#     lca = find_nearest_common_facility(root, storeId1, storeId2)
#     if lca:
#         print(f"LCA of {storeId1} and {storeId2} is: {lca.id}")
#     else:
#         print(f"LCA of {storeId1} and {storeId2} not found.")

# # Building the test binary tree
# '''
#     Tree Structure:
#           3
#          / \
#         5   1
#        / \
#       6   2
#          / \
#         7   4
# '''
# root = Store(3)
# root.left = Store(5)
# root.right = Store(1)
# root.left.left = Store(6)
# root.left.right = Store(2)
# root.left.right.left = Store(7)
# root.left.right.right = Store(4)

# # Test Case 1
# test_find_nearest_common_facility(root, 5, 1)  # Expected Output: 3

# # Test Case 2
# test_find_nearest_common_facility(root, 5, 4)  # Expected Output: 5

# # Test Case 3
# test_find_nearest_common_facility(root, 6, 4)  # Expected Output: 5

# # Test Case 4
# test_find_nearest_common_facility(root, 7, 4)  # Expected Output: 2



def beautifulNinjaFormation(n: int) -> list[int]:
    # Base cases
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]

    # Recursively generate beautiful ninja formation for odds and evens
    # Recursion ensures that no ninja satisfies 2 * nums[k] = nums[i] + nums[j]
    
    odds = beautifulNinjaFormation((n + 1) // 2)  # Odd-indexed elements
    evens = beautifulNinjaFormation(n // 2)       # Even-indexed elements

    # Construct the final array by scaling the odd part and even part
    result = [2 * x - 1 for x in odds] + [2 * x for x in evens]

    return result

# Test cases
print(beautifulNinjaFormation(4))  # Example output: [1, 3, 2, 4]
print(beautifulNinjaFormation(5))  # Example output: [1, 5, 3, 2, 4]




from collections import deque
class NodeWithBuddies:
    def _init_(self,val,left=None,right=None,next=None,prev=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        self.prev = prev

def findBuddies(rt:NodeWithBuddies) -> None:
    if not rt:
      return
    que = deque([rt])
    while que:
      levSize = len(que)
      prevNode = None
      for _ in range(levSize):
          newNode = que.popleft()
          if prevNode:
              prevNode.next = newNode
              newNode.prev = prevNode
          prevNode = newNode
          if newNode.left:
              que.append(newNode.left)
          if newNode.right:
              que.append(newNode.right)



def endgameScores(points: list[int]) -> bool:
    n = len(points)
    # Create a 2D DP array initialized to 0
    dp = [[0] * n for _ in range(n)]
    
    # Base case: when there's only one game available
    for i in range(n):
        dp[i][i] = points[i]

    # Fill the DP table
    for length in range(2, n + 1):  # length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1
            # Calculate the score difference
            dp[i][j] = max(points[i] - dp[i + 1][j], points[j] - dp[i][j - 1])
    
    # Ronaldo wins or ties if the score difference is non-negative
    return dp[0][n - 1] >= 0

# Test Cases
# print(endgameScores([3, 99, 155, 8]))  # Output: True
# print(endgameScores([5, 1, 100, 1, 5]))  # Output: False



def satisfyingOrders(X: int, k: int) -> int:
    MOD = 10**9 + 7

    # Create a DP table with (X+1) x (k+1)
    dp = [[0] * (k + 1) for _ in range(X + 1)]
    
    # Base case
    dp[1][1] = 1  # One person can satisfy themselves

    # Fill the DP table
    for i in range(2, X + 1):  # i is the number of people
        for j in range(1, k + 1):  # j is the number of satisfied people
            # If the new person is satisfied
            dp[i][j] = dp[i - 1][j - 1]  # last person satisfied
            
            # If the new person is not satisfied
            dp[i][j] += (i - 1) * dp[i - 1][j]
            dp[i][j] %= MOD

    return dp[X][k]

# Test Cases
# print(satisfyingOrders(4, 3))  # Output: 6
# print(satisfyingOrders(5, 2))  # Example case for testing




def batmanSignal(n: int):
    result = []

    def backtrack(current):
        if len(current) == n:
            result.append(current)
            return
        
        if not current or current[-1] == 'x':
            backtrack(current + 'y')  
        if not current or current[-1] == 'y' or current[-1] == 'x':
            backtrack(current + 'x')  

    backtrack("")
    
    return result

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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    # Base case: if head is None, return None
    if not head:
        return None
    
    # Recursive call for the next node
    head.next = removeElements(head.next, val)
    
    # Check the current node's value
    if head.val == val:
        # Skip this node
        return head.next
    else:
        # Keep this node
        return head

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert linked list to a list for easy display
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

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



def rearrangeAllToys(toys):
    # Sort the toys array
    toys.sort()
    n = len(toys)
    
    # Create a new array to store the rearranged toys
    rearranged = [0] * n
    
    # Find the middle index and set up two pointers
    mid = (n + 1) // 2
    left = mid - 1  # Pointer for smaller elements
    right = n - 1   # Pointer for larger elements
    
    # Fill the rearranged array in a zig-zag pattern
    for i in range(n):
        if i % 2 == 0:
            # Even index: take from the left (smaller elements)
            rearranged[i] = toys[left]
            left -= 1
        else:
            # Odd index: take from the right (larger elements)
            rearranged[i] = toys[right]
            right -= 1
    
    return rearranged

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
    if not root:
        return []

    # This will hold the nodes at each column
    column_table = defaultdict(list)
    
    # Queue for BFS
    queue = deque([(root, 0, 0)])  # (node, column_index, depth)
    
    while queue:
        node, column, depth = queue.popleft()
        
        # Append the node's value and its depth to the column table
        column_table[column].append((depth, node.val))
        
        # Add left and right children to the queue with updated column and depth
        if node.left:
            queue.append((node.left, column - 1, depth + 1))
        if node.right:
            queue.append((node.right, column + 1, depth + 1))

    # Sort the columns and then the entries within each column
    sorted_columns = sorted(column_table.keys())
    result = []
    
    for col in sorted_columns:
        # Sort by depth, then by node value
        column_nodes = sorted(column_table[col], key=lambda x: (x[0], x[1]))
        result.append([val for _, val in column_nodes])
    
    return result

# # Example usage:
# # Construct the tree from the first example
# root1 = TreeNode(3)
# root1.left = TreeNode(9)
# root1.right = TreeNode(20)
# root1.right.left = TreeNode(15)
# root1.right.right = TreeNode(7)

# print(puzzleOfTheTrees(root1))  # Output: [[9],[3,15],[20],[7]]

# # Construct the tree from the second example
# root2 = TreeNode(1)
# root2.left = TreeNode(2)
# root2.right = TreeNode(3)
# root2.left.left = TreeNode(4)
# root2.left.right = TreeNode(6)
# root2.right.left = TreeNode(5)
# root2.right.right = TreeNode(7)

# print(puzzleOfTheTrees(root2))  # Output: [[4],[2],[1,5,6],[3],[7]]

# # Construct the tree from the third example
# root3 = TreeNode(1)
# root3.left = TreeNode(2)
# root3.right = TreeNode(3)
# root3.left.left = TreeNode(4)
# root3.left.right = TreeNode(5)
# root3.right.left = TreeNode(6)
# root3.right.right = TreeNode(7)

# print(puzzleOfTheTrees(root3))  # Output: [[4],[2],[1,5,6],[3],[7]]





