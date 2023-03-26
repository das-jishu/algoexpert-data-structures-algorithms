
# MIN HEAP CONSTRUCTION

#########################################
# THIS DOES NOT WORK FOR TWO ELEMENTS IN THE HEAP. DO NOT USE THIS. USE THE ONE GIVEN BELOW.
##########################################

class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

	# O(N) time and O(1) space
    def buildHeap(self, array):
        # Write your code here.
        firstParent = (len(array) - 2) // 2
		for currentIndex in reversed(range(firstParent + 1)):
			self.siftDown(currentIndex, array)
			print(array)
		return array

	# O(log(n)) time and O(1) space
    def siftDown(self, start, array):
        # Write your code here.
        while start * 2 + 1 < len(array):
			minChild = self.findMinChild(start, array)
			if array[start] > array[minChild]:
				self.swap(start, minChild, array)
			start = minChild
			
	def findMinChild(self, n, array):
		if n * 2 + 2 >= len(array):
			return n * 2 + 1
		if array[n * 2 + 1] < array[n * 2 + 2]:
			return n * 2 + 1
		else:
			return n * 2 + 2

	# O(log(n)) time and O(1) space
    def siftUp(self, start, array):
        # Write your code here.
        while (start - 1) // 2 > 0:
			child = array[start]
			parent = array[(start - 1) // 2]
			if child < parent:
				self.swap(start, (start-1)//2, array)
			start = (start - 1) // 2
			
	def swap(self, i, j, array):
		array[i], array[j] = array[j], array[i]

	# O(1) time and space
    def peek(self):
        # Write your code here.
        return self.heap[0]

	# O(log(n)) time and O(1) space
    def remove(self):
        # Write your code here.
		self.swap(0, len(self.heap) - 1, self.heap)
        deletedValue = self.heap.pop()
		self.siftDown(0, self.heap)
		return deletedValue

	# O(log(n)) time and O(1) space
    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)

############################################
# CORRECT IMPLEMENTATION
############################################

class MinHeap:
	def __init__(self, array):
		self.heap = self.buildHeap(array)
		
	def isEmpty(self):
		return len(self.heap) == 0
	
	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
	
	def siftDown(self, currentIdx, endIdx, heap):
		childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return
			
	def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2
	
	def peek(self):
		return self.heap[0]
	
	def remove(self):
		self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove
	
	def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)
		
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]