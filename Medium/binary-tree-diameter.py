
# BINARY TREE DIAMETER

# O(N) time and O(d) space
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binaryTreeDiameter(tree):
    # Write your code here.
	longestDiameter = [0]
	binaryTreeHelper(tree, longestDiameter)
	return longestDiameter[0]
	
def binaryTreeHelper(tree, longestDiameter):
    if tree is None:
		return 0
	
	maxLeftPath = binaryTreeHelper(tree.left, longestDiameter)
	maxRightPath = binaryTreeHelper(tree.right, longestDiameter)
	maxCurrentPathLength = maxLeftPath + maxRightPath
	longestDiameter[0] = max(longestDiameter[0], maxCurrentPathLength)
	return max(1 + maxLeftPath, 1 + maxRightPath)
	
# O(N) time and O(d) space
""" # This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return getInfoTree(tree).diameter

class TreeInfo:
	def __init__(self, diameter, height):
		self.diameter = diameter
		self.height = height
		
def getInfoTree(tree):
	if tree is None:
		return TreeInfo(0, 0)
	
	leftTreeInfo = getInfoTree(tree.left)
	rightTreeInfo = getInfoTree(tree.right)
	longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
	maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
	currentDiameter = max(maxDiameterSoFar, longestPathThroughRoot)
	currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
	
	return TreeInfo(currentDiameter, currentHeight) """
	
