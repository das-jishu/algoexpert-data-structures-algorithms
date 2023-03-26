
# LONGEST INCREASING SUBSEQUENCE

# O(N^2) time and O(N) space
def longestIncreasingSubsequence(array):
    # Write your code here.
    lengths = [1 for _ in array]
	sequences = [None for _ in array]
	start, maxLength = 0, 0
	for idx in range(len(lengths)):
		for prev in range(idx):
			if array[prev] < array[idx] and lengths[prev] + 1 > lengths[idx]:
				lengths[idx] = lengths[prev] + 1
				sequences[idx] = prev
				if lengths[idx] > maxLength:
					maxLength = lengths[idx]
					start = idx
	
	return buildSequence(array, sequences, start)

def buildSequence(array, sequences, start):
	result = [array[start]]
	while sequences[start] != None:
		result.append(array[sequences[start]])
		start = sequences[start]
	return list(reversed(result))
	

# O(NlogN) time and O(N) space
def longestIncreasingSubsequence(array):
	sequences = [None for x in array]
	indices = [None for x in range(len(array) + 1)]
	length = 0
	for i, num in enumerate(array):
		newLength = binarySearch(1, length, indices, array, num)
		sequences[i] = indices[newLength - 1]
		indices[newLength] = i
		length = max(length, newLength)
	return buildSequence(array, sequences, indices[length])

def binarySearch(startIdx, endIdx, indices, array, num):
	if startIdx > endIdx:
		return startIdx
	middleIdx = (startIdx + endIdx) // 2
	if array[indices[middleIdx]] < num:
		startIdx = middleIdx + 1
	else:
		endIdx = middleIdx - 1
	return binarySearch(startIdx, endIdx, indices, array, num)

def buildSequence(array, sequences, start):
	result = [array[start]]
	while sequences[start] != None:
		result.append(array[sequences[start]])
		start = sequences[start]
	return list(reversed(result))

