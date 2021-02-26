
# RECONSTRUCT BST

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N^2) ntime and O(H) space
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    return reconstructTree(preOrderTraversalValues, 0, len(preOrderTraversalValues) - 1)

def reconstructTree(preOrderValues, start, end):
	if start > end:
		return None
	rootValue = preOrderValues[start]
	index = start + 1
	while index <= end and preOrderValues[index] < rootValue:
		index += 1
	
	leftSubtree = reconstructTree(preOrderValues, start + 1, index - 1)
	rightSubtree = reconstructTree(preOrderValues, index, end)
	root = BST(rootValue, leftSubtree, rightSubtree)
	return root

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, rootIdx):
		self.rootIdx = rootIdx
		
# O(N) time and space
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    treeInfo = TreeInfo(0)
	return reconstructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
	if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
		return None
	
	rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
	if rootValue < lowerBound or rootValue >= upperBound:
		return None
	
	currentSubtreeInfo.rootIdx += 1
	leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
	rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)
	return BST(rootValue, leftSubtree, rightSubtree)

