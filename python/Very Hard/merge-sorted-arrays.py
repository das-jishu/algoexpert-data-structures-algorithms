
# MERGE SORTED ARRAYS

# O(NK) time and O(N + K) space
def mergeSortedArrays(arrays):
    # Write your code here.
    mergedArray = []
	pointers = [0 for _ in arrays]
	while True:
		smallest = []
		for index in range(len(arrays)):
			currentArray = arrays[index]
			currentPointer = pointers[index]
			if currentPointer >= len(currentArray):
				continue
			smallest.append({"idx": index, "num": currentArray[currentPointer]})
		if len(smallest) == 0:
			break
		minimum = getMin(smallest)
		mergedArray.append(minimum["num"])
		pointers[minimum["idx"]] += 1
	return mergedArray

def getMin(smallest):
	minimum = float("inf")
	minEl = {}
	for elem in smallest:
		if elem["num"] < minimum:
			minimum = elem["num"]
			minEl = elem
	return minEl
	

# O(NlogK + K) time and O(N + K) space
def mergeSortedArrays(arrays):
    # Write your code here.
    mergedArray = []
	smallest = []
	for index in range(len(arrays)):
		smallest.append({"arrayIdx": index, "elemIndex": 0, "num": arrays[index][0]})
	minHeap = MinHeap(smallest)
	while not minHeap.isEmpty():
		smallestElement = minHeap.remove()
		mergedArray.append(smallestElement["num"])
		arrayIdx = smallestElement["arrayIdx"]
		elementIdx = smallestElement["elemIndex"]
		if elementIdx >= len(arrays[arrayIdx]) - 1:
			continue
		minHeap.insert({"arrayIdx": arrayIdx, "elemIndex": elementIdx + 1, "num": arrays[arrayIdx][elementIdx + 1]})
	return mergedArray

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
			if childTwoIdx != -1 and heap[childTwoIdx]["num"] < heap[childOneIdx]["num"]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap]["num"] < heap[currentIdx]["num"]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return
			
	def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx]["num"] < heap[parentIdx]["num"]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2
			
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
			
		
