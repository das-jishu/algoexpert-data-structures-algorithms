
# FIND KTH LARGEST VALUE IN BST

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(H + K) time and O(H) space
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    numberOfNodes = countNodes(tree)
	k = numberOfNodes - k
	return kthInorderValue(tree, k)

def kthInorderValue(tree, k):
	stack = []
	current = tree
	while True:
		if current is not None:
			stack.append(current)
			current = current.left
		else:
			if len(stack) == 0:
				break
			temporaryNode = stack.pop()
			if k == 0:
				return temporaryNode.value
			k -= 1
			current = temporaryNode.right
	return current.value
	
def countNodes(tree):
	if tree is None:
		return 0
	return 1 + countNodes(tree.left) + countNodes(tree.right)

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
		self.numberOfNodesVisited = numberOfNodesVisited
		self.latestVisitedNodeValue = latestVisitedNodeValue

# O(H + K) time and O(H) space
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    treeInfo = TreeInfo(0, -1)
	reverseInorderTraverse(tree, k, treeInfo)
	return treeInfo.latestVisitedNodeValue

def reverseInorderTraverse(node, k, treeInfo):
	if node is None or treeInfo.numberOfNodesVisited >= k:
		return
	
	reverseInorderTraverse(node.right, k, treeInfo)
	if treeInfo.numberOfNodesVisited < k:
		treeInfo.numberOfNodesVisited += 1
		treeInfo.latestVisitedNodeValue = node.value
		reverseInorderTraverse(node.left, k, treeInfo)
		
		
