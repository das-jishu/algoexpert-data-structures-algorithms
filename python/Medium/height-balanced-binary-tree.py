
# HEIGHT BALANCED BINARY TREE

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self, leftTreeHeight, rightTreeHeight, isHeightBalanced):
		self.leftTreeHeight = leftTreeHeight
		self.rightTreeHeight = rightTreeHeight
		self.isHeightBalanced = isHeightBalanced
		
# O(N) time and O(h) space
def heightBalancedBinaryTree(tree):
    # Write your code here.
    return heightBalancedHelper(tree).isHeightBalanced

def heightBalancedHelper(tree):
	if tree is None:
		return TreeInfo(0, 0, True)
	
	leftTreeInfo = heightBalancedHelper(tree.left)
	rightTreeInfo = heightBalancedHelper(tree.right)
	leftTreeHeight = max(leftTreeInfo.leftTreeHeight, leftTreeInfo.rightTreeHeight) + 1
	rightTreeHeight = max(rightTreeInfo.leftTreeHeight, rightTreeInfo.rightTreeHeight) + 1
	isHeightBalanced = abs(leftTreeHeight - rightTreeHeight) <= 1 and leftTreeInfo.isHeightBalanced and rightTreeInfo.isHeightBalanced
	return TreeInfo(leftTreeHeight, rightTreeHeight, isHeightBalanced)
	
