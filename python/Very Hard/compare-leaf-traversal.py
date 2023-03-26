
# COMPARE LEAF TRAVERSAL

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N + M) time and O(max(H1, H2)) space
def compareLeafTraversal(tree1, tree2):
    # Write your code here.
	list1, _ = connectLeafNodes(tree1)
	list2, _ = connectLeafNodes(tree2)
	
	current1 = list1
	current2 = list2
	while current1 is not None and current2 is not None:
		if current1.value != current2.value:
			return False
		
		current1 = current1.right
		current2 = current2.right
		
	return current1 is None and current2 is None

def connectLeafNodes(currentNode, head=None, previousNode=None):
	if currentNode is None:
		return head, previousNode
	
	if isLeafNode(currentNode):
		if previousNode is None:
			head = currentNode
		else:
			previousNode.right = currentNode
			
		previousNode = currentNode
		
	leftHead, leftPreviousNode = connectLeafNodes(currentNode.left, head, previousNode)
	return connectLeafNodes(currentNode.right, leftHead, leftPreviousNode)

def isLeafNode(node):
	return node.left is None and node.right is None