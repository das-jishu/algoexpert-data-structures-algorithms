
""" 
# FIND CLOSEST VALUE IN BST

Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that target value contained in the BST.

"""


def findClosestValueInBst(tree, target):
    # Write your code here.
    # Iterative way, can be also done recursively.
	if not tree:
		return 0
	
	value = tree.value
	while tree:
		if tree.value == target:
			return target
		current_difference = abs(tree.value - target)
		min_difference = abs(value - target)
		if current_difference < min_difference:
			value = tree.value
		if target >= tree.value:
			tree = tree.right
		else:
			tree = tree.left
			
	return value

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
