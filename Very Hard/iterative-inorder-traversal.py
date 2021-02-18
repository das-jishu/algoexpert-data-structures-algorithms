
# ITERATIVE IN-ORDER TRAVERSAL

# O(N) time and space
def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
    stackOfNodes = []
	currentNode = tree
	while True:
		if currentNode:
			stackOfNodes.append(currentNode)
			currentNode = currentNode.left
			
		else:
			if len(stackOfNodes) == 0:
				break
			temporaryNode = stackOfNodes.pop()
			callback(temporaryNode)
			currentNode = temporaryNode.right
		

# O(N) time and O(1) space
def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
	previousNode = None
	currentNode = tree
	while currentNode is not None:
		if previousNode is None or previousNode == currentNode.parent:
			if currentNode.left is not None:
				nextNode = currentNode.left
			else:
				callback(currentNode)
				nextNode = currentNode.right if currentNode.right else currentNode.parent
				
		elif previousNode == currentNode.left:
			callback(currentNode)
			nextNode = currentNode.right if currentNode.right else currentNode.parent
		else:
			nextNode = currentNode.parent
		previousNode = currentNode
		currentNode = nextNode
		
    
