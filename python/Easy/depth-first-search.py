
# DEPTH FIRST SEARCH

# ITERATIVE WAY
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
		stack = [self]
		while stack:
			vertex = stack.pop()
			array.append(vertex.name)
			for child in vertex.children[::-1]:
				stack.append(child)
		return array

# RECURSIVE WAY
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
			
		return array
