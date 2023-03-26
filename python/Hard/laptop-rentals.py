
# LAPTOP RENTALS

# O(NlogN) time and O(N) space
def laptopRentals(times):
    # Write your code here.
    start = [time[0] for time in times]
	end = [time[1] for time in times]
	start.sort()
	end.sort()
	
	i, j = 0, 0
	laptops = 0
	while i < len(start):
		if start[i] < end[j]:
			laptops += 1
			i += 1
		else:
			i += 1
			j += 1
			
	return laptops
			
# O(NlogN) time and O(N) space
def laptopRentals(times):
    # Write your code here.
    if len(times) == 0:
		return 0
	
	times.sort(key=lambda x: x[0])
	timesWhenLaptopIsUsed = [times[0]]
	heap = MinHeap(timesWhenLaptopIsUsed)
	
	for idx in range(1, len(times)):
		currentInterval = times[idx]
		if heap.peek()[1] <= currentInterval[0]:
			heap.remove()
			
		heap.insert(currentInterval)
		
	return len(timesWhenLaptopIsUsed)

class MinHeap:
	def __init__(self, array):
		self.heap = self.buildHeap(array)
		
	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array
	
	def siftDown(self, currentIdx, endIdx, heap):
		childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap][1] < heap[currentIdx][1]:
				self.swap(currentIdx, idxToSwap, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return
			
	def siftUp(self, currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
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
