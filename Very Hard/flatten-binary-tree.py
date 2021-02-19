
# FLATTEN BINARY TREE

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N) time and space
def flattenBinaryTree(root):
    # Write your code here.
	inOrderArray = []
    getNodesInOrder(root, inOrderArray)
	for i in range(len(inOrderArray) - 1):
		leftNode = inOrderArray[i]
		rightNode = inOrderArray[i + 1]
		leftNode.right = rightNode
		rightNode.left = leftNode
	return inOrderArray[0]

def getNodesInOrder(tree, array):
	if tree is None:
		return
	getNodesInOrder(tree.left, array)
	array.append(tree)
	getNodesInOrder(tree.right, array)
		

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N) time and O(d) space
def flattenBinaryTree(root):
    # Write your code here.
    #inOrderTraverse(root, None)
	stackOfNodes = []
	currentNode = root
	previousInorderNode = None
	print("here")
	while True:
		if currentNode:
			stackOfNodes.append(currentNode)
			currentNode = currentNode.left
			
		else:
			if len(stackOfNodes) == 0:
				break
			temporaryNode = stackOfNodes.pop()
			temporaryNode.left = previousInorderNode
			previousInorderNode = temporaryNode
			
			currentNode = temporaryNode.right
	
	while previousInorderNode.left is not None:
		temporaryNode = previousInorderNode.left
		temporaryNode.right = previousInorderNode
		previousInorderNode = previousInorderNode.left
	
	return previousInorderNode

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N) time and O(D) space
def flattenBinaryTree(root):
    # Write your code here.
    leftMost, _ = flattenTree(root)
	return leftMost

def flattenTree(node):
	if node.left is None:
		leftMost = node
	else:
		leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
		connectNodes(leftSubtreeRightMost, node)
		leftMost = leftSubtreeLeftMost
		
	if node.right is None:
		rightMost = node
	else:
		rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
		connectNodes(node, rightSubtreeLeftMost)
		rightMost = rightSubtreeRightMost
		
	return [leftMost, rightMost]

def connectNodes(left, right):
	left.right = right
	right.left = left
