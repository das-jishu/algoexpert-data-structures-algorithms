
# BREADTH FIRST SEARCH

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

	# O(V+E) time, O(V) space
    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]
		while queue:
			currentNode = queue.pop(0)
			array.append(currentNode.name)
			for child in currentNode.children:
				queue.append(child)
		return array
