
# FIND SUCCESSOR

# O(h) time and O(1) space
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right != None:
		current = node.right
		while current.left:
			current = current.left
		return current
	
	else:
		if not node.parent:
			return None
		current = node
		while current.parent:
			if current.parent.left == current:
				return current.parent
			current = current.parent
		return None
