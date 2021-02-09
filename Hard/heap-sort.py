
# HEAP SORT

# BEST, AVERAGE, WORST: O(nlogn) time, O(1) space
def heapSort(array):
    # Write your code here.
    buildHeap(array)
	for endidx in reversed(range(1, len(array))):
		swap(0, endidx, array)
		siftDown(0, endidx - 1, array)
	return array
	
def buildHeap(array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx + 1)):
			siftDown(currentIdx, len(array) - 1, array)
	
def siftDown(currentIdx, endIdx, heap):
	childOneIdx = currentIdx * 2 + 1
	while childOneIdx <= endIdx:
		childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
		if childTwoIdx != -1:
			if heap[childTwoIdx] > heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
		else:
			idxToSwap = childOneIdx
		if heap[idxToSwap] > heap[currentIdx]:
			swap(currentIdx, idxToSwap, heap)
			currentIdx = idxToSwap
			childOneIdx = currentIdx * 2 + 1
		else:
			return
		
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]