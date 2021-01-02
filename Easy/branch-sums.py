
""" 
# BRANCH SUMS

Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum. A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node. 
"""


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	result = []
	calculateBranchSums(root, 0, result)
	return result

def calculateBranchSums(root, currentSum, result):
	if not root:
		return
	
	newSum = currentSum + root.value
	if not root.left and not root.right:
		result.append(newSum)
		return
 
	calculateBranchSums(root.left, newSum, result)
	calculateBranchSums(root.right, newSum, result)

	
		
