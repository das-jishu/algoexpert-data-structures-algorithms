
# SUBARRAY SORT

# O(NlogN) time and O(N) space
def subarraySort(array):
    # Write your code here.
    sortedArray = sorted(array)
	indices = []
	i = 0
	while i < len(array):
		if array[i] != sortedArray[i]:
			indices.append(i)
		i += 1
			
	return [-1, -1] if not indices else [indices[0], indices[len(indices) - 1]]

# O(N) time and O(1) space
def subarraySort(array):
    # Write your code here.
    indices = [-1, -1]
	index = 1
	while index < len(array) and array[index] >= array[index-1]:
		index += 1
	if index == len(array):
		return indices
	currentMin = array[index]
	j = index + 1
	while j < len(array):
		currentMin = min(currentMin, array[j])
		j += 1
	index -= 1
	while index >= 0 and currentMin < array[index]:
		index -= 1
	indices[0] = index + 1
		
	index = len(array) - 2
	while index >= 0 and array[index] <= array[index+1]:
		index -= 1
			
	currentMax = array[index]
	j = index - 1
	while j >= 0:
		currentMax = max(currentMax, array[j])
		j -= 1
	index += 1
	while index < len(array) and currentMax > array[index]:
		index += 1
	indices[1] = index - 1
	return indices

# O(N) time and O(1) space		
def subarraySort(array):
    # Write your code here.
    minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	for i in range(len(array)):
		num = array[i]
		if isOutOfOrder(i, num, array):
			minOutOfOrder = min(minOutOfOrder, num)
			maxOutOfOrder = max(maxOutOfOrder, num)
	if minOutOfOrder == float("inf"):
		return [-1, -1]
	subarrayLeftIdx = 0
	while minOutOfOrder >= array[subarrayLeftIdx]:
		subarrayLeftIdx += 1
	subarrayRightIdx = len(array) - 1
	while maxOutOfOrder <= array[subarrayRightIdx]:
		subarrayRightIdx -= 1
	return [subarrayLeftIdx, subarrayRightIdx]

def isOutOfOrder(i, num, array):
	if i == 0:
		return num > array[i+1]
	if i == len(array) - 1:
		return num < array[i-1]
	return num > array[i + 1] or num < array[i-1]