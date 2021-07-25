
# SUBTREES WITHIN RANGE

# O(N) time and O(H) space, where N -> total no.of nodes in the tree
# H -> height of the tree.
def subtreesWithinRange(tree, targetRange):
    # Write your code here.
    return findValidTrees(tree, targetRange).count

def findValidTrees(root, targetRange):
	if root == None:
		return TreeInfo(True, 0)
	
	leftSubtreeInfo = findValidTrees(root.left, targetRange)
	rightSubtreeInfo = findValidTrees(root.right, targetRange)
	
	isValidSubtree = targetRange[0] <= root.value <= targetRange[1] and leftSubtreeInfo.isValidTree and rightSubtreeInfo.isValidTree
	currentCount = leftSubtreeInfo.count + rightSubtreeInfo.count
	currentCount = currentCount + 1 if isValidSubtree else currentCount 
	return TreeInfo(isValidSubtree, currentCount)		

class TreeInfo:
	def __init__(self, isValidTree, count):
		self.isValidTree = isValidTree
		self.count = count

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
