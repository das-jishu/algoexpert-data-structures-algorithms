
# RIGHT SMALLER THAN

# O(N^2) time and O(N) space
def rightSmallerThan(array):
    # Write your code here.
    output = []
	for i, x in enumerate(array):
		count, index = 0, i + 1
		while index < len(array):
			if array[index] < x:
				count += 1
			index += 1
		output.append(count)
	return output

# Average and Best: O(NlogN) time and O(N) space
# Worst: O(N^2) time and O(N) space
def rightSmallerThan(array):
    # Write your code here.
    if len(array) == 0:
		return []
	lastIdx = len(array) - 1
	bst = SpecialBST(array[lastIdx], lastIdx, 0)
	for i in reversed(range(len(array) - 1)):
		bst.insert(array[i], i)
		
	rightSmallerCounts = array[:]
	getRightSmallerCounts(bst, rightSmallerCounts)
	return rightSmallerCounts

def getRightSmallerCounts(bst, rightSmallerCounts):
	if bst is None:
		return
	rightSmallerCounts[bst.idx] = bst.numSmallerAtInsertTime
	getRightSmallerCounts(bst.left, rightSmallerCounts)
	getRightSmallerCounts(bst.right, rightSmallerCounts)
	
class SpecialBST:
	def __init__(self, value, idx, numSmallerAtInsertTime):
		self.value = value
		self.idx = idx
		self.numSmallerAtInsertTime = numSmallerAtInsertTime
		self.leftSubtreeSize = 0
		self.left = None
		self.right = None
	
	def insert(self, value, idx, numSmallerAtInsertTime=0):
		if value < self.value:
			self.leftSubtreeSize += 1
			if self.left is None:
				self.left = SpecialBST(value, idx, numSmallerAtInsertTime)
			else:
				self.left.insert(value, idx, numSmallerAtInsertTime)
		else:
			numSmallerAtInsertTime += self.leftSubtreeSize
			if value > self.value:
				numSmallerAtInsertTime += 1
			if self.right is None:
				self.right = SpecialBST(value, idx, numSmallerAtInsertTime)
			else:
				self.right.insert(value, idx, numSmallerAtInsertTime)
				
# Average and Best: O(NlogN) time and O(N) space
# Worst: O(N^2) time and O(N) space
def rightSmallerThan(array):
    # Write your code here.
    if len(array) == 0:
		return []
	lastIdx = len(array) - 1
	rightSmallerCounts = array[:]
	bst = SpecialBST(array[lastIdx])
	rightSmallerCounts[lastIdx] = 0
	for i in reversed(range(len(array) - 1)):
		bst.insert(array[i], i, rightSmallerCounts)
		
	return rightSmallerCounts

class SpecialBST:
	def __init__(self, value):
		self.value = value
		self.leftSubtreeSize = 0
		self.left = None
		self.right = None
	
	def insert(self, value, idx, rightSmallerCounts, numSmallerAtInsertTime=0):
		if value < self.value:
			self.leftSubtreeSize += 1
			if self.left is None:
				self.left = SpecialBST(value)
				rightSmallerCounts[idx] = numSmallerAtInsertTime
			else:
				self.left.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)
		else:
			numSmallerAtInsertTime += self.leftSubtreeSize
			if value > self.value:
				numSmallerAtInsertTime += 1
			if self.right is None:
				self.right = SpecialBST(value)
				rightSmallerCounts[idx] = numSmallerAtInsertTime
			else:
				self.right.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)
				
