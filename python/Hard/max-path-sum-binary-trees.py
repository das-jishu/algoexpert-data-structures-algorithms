
# MAX PATH SUM IN BINARY TREES

# O(N) time and space
def maxPathSum(tree):
    # Write your code here.
	root = calculateMaxPathSum(tree)
	return root.maxPathSum
	
def calculateMaxPathSum(node):
	if not node:
		return TreeInfo()
	
	leftSubtree = calculateMaxPathSum(node.left)
	rightSubtree = calculateMaxPathSum(node.right)
	maxLeftPathSum = max(leftSubtree.maxLeftSum + node.value, leftSubtree.maxRightSum + node.value)
	maxRightPathSum = max(rightSubtree.maxLeftSum + node.value, rightSubtree.maxRightSum + node.value)
	currentMaxPathSum = maxLeftPathSum + maxRightPathSum - node.value
	maxPathSumFromSubtrees = max(leftSubtree.maxPathSum, rightSubtree.maxPathSum)
	maxPathSumFromCurrentNode = max(currentMaxPathSum, maxPathSumFromSubtrees, maxLeftPathSum, maxRightPathSum)
	newNode = TreeInfo()
	newNode.maxLeftSum = maxLeftPathSum
	newNode.maxRightSum = maxRightPathSum
	newNode.maxPathSum = maxPathSumFromCurrentNode
	return newNode
    
class TreeInfo:
	def __init__(self):
		self.maxLeftSum = 0
		self.maxRightSum = 0
		self.maxPathSum = float('-inf')


# O(N) time and space
def maxPathSum(tree):
    # Write your code here.
	root = calculateMaxPathSum(tree)
	return root.maxPathSum
	
def calculateMaxPathSum(node):
	if not node:
		return TreeInfo()
	
	leftSubtree = calculateMaxPathSum(node.left)
	rightSubtree = calculateMaxPathSum(node.right)
	leftPathSum = leftSubtree.maxPathSumUsingCurrentNode + node.value
	rightPathSum = rightSubtree.maxPathSumUsingCurrentNode + node.value
	maxPathSumUsingCurrentNode = max(leftPathSum, rightPathSum)
	
	currentMaxPathSum = leftPathSum + rightPathSum - node.value
	maxPathSumFromSubtrees = max(leftSubtree.maxPathSum, rightSubtree.maxPathSum)
	maxPathSum = max(currentMaxPathSum, maxPathSumFromSubtrees, maxPathSumUsingCurrentNode)
	newNode = TreeInfo()
	newNode.maxPathSumUsingCurrentNode = maxPathSumUsingCurrentNode
	newNode.maxPathSum = maxPathSum
	return newNode
    
class TreeInfo:
	def __init__(self):
		self.maxPathSumUsingCurrentNode = 0
		self.maxPathSum = float('-inf')


# O(logN) space, O(N) time
def maxPathSum(tree):
    # Write your code here.
	root = calculateMaxPathSum(tree)
	return root[1]
	
def calculateMaxPathSum(node):
	if not node:
		return [0, float('-inf')]
	
	leftSubtree = calculateMaxPathSum(node.left)
	rightSubtree = calculateMaxPathSum(node.right)
	leftPathSum = leftSubtree[0] + node.value
	rightPathSum = rightSubtree[0] + node.value
	maxPathSumUsingCurrentNode = max(leftPathSum, rightPathSum)
	
	currentMaxPathSum = leftPathSum + rightPathSum - node.value
	maxPathSumFromSubtrees = max(leftSubtree[1], rightSubtree[1])
	maxPathSum = max(currentMaxPathSum, maxPathSumFromSubtrees, maxPathSumUsingCurrentNode)
	
	return [maxPathSumUsingCurrentNode, maxPathSum]
    