def leafSum(root) -> int:

    return depthFirstSearch(root, 0)


def depthFirstSearch(node, sum):

    if(node == None):
        return 0

    sum = sum*10 + node.val

    if(node.left == None and node.right == None):
        return sum
    
    leftSum = depthFirstSearch(node.left, sum)
    rightSum = depthFirstSearch(node.right, sum)

    return(leftSum+rightSum)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root1 = TreeNode(4)
root1.left = TreeNode(9)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(1)
root1.right = TreeNode(0)
# root1.right.left = TreeNode(0)
print(leafSum(root1))  