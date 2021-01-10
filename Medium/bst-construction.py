
# BST CONSTRUCTION

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		if not self:
			return BST(value)
		
		current = self
		while current:
			if value < current.value:
				if current.left:
					current = current.left
				else:
					current.left = BST(value)
					break
			else:
				if current.right:
					current = current.right
				else:
					current.right = BST(value)
					break
        return self

    def contains(self, value):
        # Write your code here.
        current = self
		while current:
			if value == current.value:
				return True
			elif value < current.value:
				current = current.left
			else:
				current = current.right
		return False
	
	def getMin(self):
		current = self
		while current.left is not None:
			current = current.left
		return current.value

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
		if value < self.value:
			if self.left:
				self.left.remove(value, self)
		elif value > self.value:
			if self.right:
				self.right.remove(value, self)
		else:
			if self.left is not None and self.right is not None:
				self.value = self.right.getMin()
				self.right.remove(self.value, self)
			elif self.left is None and self.right is None:
				if not parent:
					pass
				else:
					if parent.left == self:
						parent.left = None
					else:
						parent.right = None
			elif self.left is None:
				if not parent:
					self.value = self.right.value
					self.left = self.right.left
					self.right = self.right.right
				else:
					if parent.left == self:
						parent.left = self.right
					else:
						parent.right = self.right
			else:
				if not parent:
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				else:
					if parent.left == self:
						parent.left = self.left
					else:
						parent.right = self.left
		
			

# SECOND WAY

"""
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
		self.parent = parent

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		if not self:
			return BST(value)
		
		current = self
		while current:
			if value < current.value:
				if current.left:
					current = current.left
				else:
					current.left = BST(value, current)
					break
			else:
				if current.right:
					current = current.right
				else:
					current.right = BST(value, current)
					break
        return self

    def contains(self, value):
        # Write your code here.
        current = self
		while current:
			if value == current.value:
				return True
			elif value < current.value:
				current = current.left
			else:
				current = current.right
		return False
	
	def getMin(self):
		current = self
		while current.left is not None:
			current = current.left
		return current

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		toBeDeleted = self
		while toBeDeleted and toBeDeleted.value != value:
			if value < toBeDeleted.value:
				toBeDeleted = toBeDeleted.left
			else:
				toBeDeleted = toBeDeleted.right
				
		print('Deleting', value)
		if toBeDeleted.parent:
			print('Found node', toBeDeleted.value, 'with parent', toBeDeleted.parent.value)
		if toBeDeleted.left is None and toBeDeleted.right is None:
			if not toBeDeleted.parent:
				pass
			else:
				if toBeDeleted.parent.left == toBeDeleted:
					toBeDeleted.parent.left = None
				else:
					toBeDeleted.parent.right = None
		
		elif toBeDeleted.left is None:
			if not toBeDeleted.parent:
				self.value = self.right.value
				self.left = self.right.left
				self.right = self.right.right
			else:
				if toBeDeleted.parent.left == toBeDeleted:
					toBeDeleted.parent.left = toBeDeleted.right
					toBeDeleted.right.parent = toBeDeleted.parent
				else:
					toBeDeleted.parent.right = toBeDeleted.right
					toBeDeleted.right.parent = toBeDeleted.parent
				
		elif toBeDeleted.right is None:
			if not toBeDeleted.parent:
				self.value = self.left.value
				self.right = self.left.right
				self.left = self.left.left
			else:
				if toBeDeleted.parent.left == toBeDeleted:
					toBeDeleted.parent.left = toBeDeleted.left
					toBeDeleted.left.parent = toBeDeleted.parent
				else:
					toBeDeleted.parent.right = toBeDeleted.left
					toBeDeleted.left.parent = toBeDeleted.parent
				
		else:
			successor = toBeDeleted.right.getMin()
			toBeDeleted.value = successor.value
			toBeDeleted.right.remove(successor.value)
"""	
