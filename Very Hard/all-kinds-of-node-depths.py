
# ALL KINDS OF NODE DEPTHS

# O(N) time and O(H) space
def allKindsOfNodeDepths(root):
    # Write your code here.
    return sumOfNodeDepths(root)

def sumOfNodeDepths(root, currentDepth=0):
	if root is None:
		return 0
	left = sumOfNodeDepths(root.left, currentDepth + 1)
	right = sumOfNodeDepths(root.right, currentDepth + 1)
	totalDepthOfCurrentNode = (currentDepth * (currentDepth + 1) / 2)
	sumOfDepths = totalDepthOfCurrentNode + left + right
	return sumOfDepths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(N) time and O(H) space
def allKindsOfNodeDepths(root):
    # Write your code here.
    return getTreeInfo(root).sumOfAllDepths

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0, 0, 0)
	
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numNodesInTree
	sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numNodesInTree
	
	numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodesInTree
	sumOfDepths = sumOfLeftDepths + sumOfRightDepths
	sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths
	
	return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths)

class TreeInfo:
	def __init__(self, numNodesInTree, sumOfDepths, sumOfAllDepths):
		self.numNodesInTree = numNodesInTree
		self.sumOfDepths = sumOfDepths
		self.sumOfAllDepths = sumOfAllDepths
		


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(N) time and space
def allKindsOfNodeDepths(root):
    # Write your code here.
    nodeCounts = {}
	addNodeCounts(root, nodeCounts)
	nodeDepths = {}
	addNodeDepths(root, nodeDepths, nodeCounts)
	return sumAllNodeDepths(root, nodeDepths)

def sumAllNodeDepths(node, nodeDepths):
	if node is None:
		return 0
	return sumAllNodeDepths(node.left, nodeDepths) + sumAllNodeDepths(node.right, nodeDepths) + nodeDepths[node]

def addNodeDepths(node, nodeDepths, nodeCounts):
	nodeDepths[node] = 0
	if node.left is not None:
		addNodeDepths(node.left, nodeDepths, nodeCounts)
		nodeDepths[node] += nodeDepths[node.left] + nodeCounts[node.left]
	if node.right is not None:
		addNodeDepths(node.right, nodeDepths, nodeCounts)
		nodeDepths[node] += nodeDepths[node.right] + nodeCounts[node.right]
		
def addNodeCounts(node, nodeCounts):
	nodeCounts[node] = 1
	if node.left is not None:
		addNodeCounts(node.left, nodeCounts)
		nodeCounts[node] += nodeCounts[node.left]
	if node.right is not None:
		addNodeCounts(node.right, nodeCounts)
		nodeCounts[node] += nodeCounts[node.right]


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
