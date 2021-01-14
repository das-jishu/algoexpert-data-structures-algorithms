
# YOUNGEST COMMON ANCESTOR

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(D) time and space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    visited = set()
	while descendantOne != topAncestor:
		visited.add(descendantOne)
		descendantOne = descendantOne.ancestor
		
	while descendantTwo != topAncestor:
		if descendantTwo in visited:
			return descendantTwo
		descendantTwo = descendantTwo.ancestor
		
	return topAncestor

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(D) time and O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depthOne = 0
	depthTwo = 0
	tempOne = descendantOne
	tempTwo = descendantTwo
	
	while descendantOne != topAncestor:
		depthOne += 1
		descendantOne = descendantOne.ancestor
		
	while descendantTwo != topAncestor:
		depthTwo += 1
		descendantTwo = descendantTwo.ancestor
		
	deeperNode = tempOne if depthOne > depthTwo else tempTwo
	shallowNode = tempOne if depthOne <= depthTwo else tempTwo
	
	i = 0
	while i < abs(depthOne - depthTwo):
		deeperNode = deeperNode.ancestor
		i += 1
	
	while deeperNode != None:
		if deeperNode == shallowNode:
			return deeperNode
		deeperNode = deeperNode.ancestor
		shallowNode = shallowNode.ancestor
		
	return None