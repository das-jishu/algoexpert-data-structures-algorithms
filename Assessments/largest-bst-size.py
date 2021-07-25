
# LARGEST BST SIZE

# O(n) time and O(h) space, n -> number of nodes, h -> height of tree
def largestBstSize(tree):
    # Write your code here.
    totalNodes, largestSize, isBST = getLargest(tree)
	return largestSize
	
def getLargest(node):
	if node == None:
		return (0, 0, True)
	
	left = node.left.value if node.left is not None else float("-inf")
	right = node.right.value if node.right is not None else float("inf")
	countLeft, largestLeft, isLeftBST = getLargest(node.left)
	countRight, largestRight, isRightBST = getLargest(node.right)
	
	if left < node.value <= right and isLeftBST and isRightBST:
		totalCount = countLeft + countRight + 1
		return (totalCount, totalCount, True)
	
	else:
		return (0, max(largestLeft, largestRight), False)


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
