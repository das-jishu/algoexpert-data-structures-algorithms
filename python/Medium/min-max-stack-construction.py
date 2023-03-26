
# MIN MAX STACK CONSTRUCTION

# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.minMaxStack = []
		self.stack = []
		
	# O(1) time and space
    def peek(self):
        # Write your code here.
        return self.stack[-1]

	# O(1) time and space
    def pop(self):
        # Write your code here.
		self.minMaxStack.pop()
        return self.stack.pop()

	# O(1) time and space
    def push(self, number):
        # Write your code here.
        self.stack.append(number)
		if len(self.minMaxStack) == 0:
			self.minMaxStack.append([number, number])
		else:
			currentMin = self.minMaxStack[-1][0]
			currentMax = self.minMaxStack[-1][1]
			if number < currentMin:
				self.minMaxStack.append([number, currentMax])
			elif number > currentMax:
				self.minMaxStack.append([currentMin, number])
			else:
				self.minMaxStack.append([currentMin, currentMax])
		
	# O(1) time and space
    def getMin(self):
        # Write your code here.
        return self.minMaxStack[-1][0]

	# O(1) time and space
    def getMax(self):
        # Write your code here.
        return self.minMaxStack[-1][1]
