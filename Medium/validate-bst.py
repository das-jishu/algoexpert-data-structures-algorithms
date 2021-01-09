
# VALIDATE BST

# O(N) time and O(logN) space or O(d) space, d -> height of BST
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
	return validateBstHelper(tree, float('-inf'), float('inf'))
    
def validateBstHelper(tree, minValue, maxValue):
	if not tree:
		return True
	
	if not minValue <= tree.value < maxValue:
		return False
	
	return validateBstHelper(tree.left, minValue, tree.value) and validateBstHelper(tree.right, tree.value, maxValue)
