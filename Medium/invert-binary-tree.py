
# INVERT BINARY TREE

# O(N) time and O(d) space
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
    	return
        
	tempLeft = tree.left
	tree.left = invertBinaryTree(tree.right)
	tree.right = invertBinaryTree(tempLeft)
	return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(N) time and O(d) space
""" def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
		return
	
	tempLeft = tree.left
	tree.left = tree.right
	tree.right = tempLeft
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
	return tree

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None """

# O(N) time and space
""" def invertBinaryTree(tree):
    # Write your code here.
    queue = [tree]
	while len(queue) > 0:
		currentNode = queue.pop()
		if currentNode is None:
			continue
		currentNode.left, currentNode.right = currentNode.right, currentNode.left
		queue.append(currentNode.left)
		queue.append(currentNode.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None """
