
# NODE DEPTHS

# SOLUTION 1
def nodeDepths(root):
    # Write your code here.
    return calculateNodeDepths(root, 0)

def calculateNodeDepths(root, currentDepth):
	if not root:
		return 0
	
	return currentDepth + calculateNodeDepths(root.left, currentDepth + 1) + calculateNodeDepths(root.right, currentDepth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# SOLUTION 2
def nodeDepths(root):
    # Write your code here.
	if not root:
		return 0
	totalDepth = 0
	currentDepth = 0
    levelOrderQueue = [root]
	while levelOrderQueue:
		totalDepth += len(levelOrderQueue) * currentDepth
		currentDepth += 1
		tempQueue = []
		while levelOrderQueue:
			tempNode = levelOrderQueue.pop()
			if tempNode.left:
				tempQueue.append(tempNode.left)
			if tempNode.right:
				tempQueue.append(tempNode.right)
		levelOrderQueue = tempQueue
		
	return totalDepth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#SOLUTION 3
def nodeDepths(root):
    # Write your code here.
    stack = [{"node": root, "depth": 0}]
	totalDepth = 0
	while len(stack) > 0:
		print(stack)
		tempNode = stack.pop()
		if not tempNode["node"]:
			continue
		totalDepth += tempNode["depth"]
		stack.append({"node": tempNode["node"].left, "depth": tempNode["depth"] + 1})
		stack.append({"node": tempNode["node"].right, "depth": tempNode["depth"] + 1})
	return totalDepth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None