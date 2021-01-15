
# LINKED LIST CONSTRUCTION

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # ALL METHODS ARE O(1) time and space unless mentioned otherwise
    def setHead(self, node):
        # Wrie your code here.
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.insertBefore(self.head, node)
			
    def setTail(self, node):
        # Write your code here.
		if self.tail is None:
			self.head = node
			self.tail = node	
		else:
			self.insertAfter(self.tail, node)
		

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		
		self.remove(nodeToInsert)
		nodeToInsert.next = node
		nodeToInsert.prev = node.prev
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert
		
		

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

	# O(P) time and O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
			self.setHead(nodeToInsert)
			return
		node = self.head
		currentPosition = 1
		while node is not None and currentPosition < position:
			node = node.next
			currentPosition += 1
		
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)

	# O(N) time and O(1) space
    def removeNodesWithValue(self, value):
        # Write your code here.
        currentNode = self.head
		while currentNode != None:
			nextNode = currentNode.next
			if currentNode.value == value:
				self.remove(currentNode)
			currentNode = nextNode

    def remove(self, node):
        # Write your code here.
		if node == self.head:
			self.head = node.next
		if node == self.tail:
			self.tail = node.prev
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None

	# O(N) time and O(1) space
    def containsNodeWithValue(self, value):
        # Write your code here.
        currentNode = self.head
		while currentNode != None:
			if currentNode.value == value:
				return True
			currentNode = currentNode.next	
		return False
