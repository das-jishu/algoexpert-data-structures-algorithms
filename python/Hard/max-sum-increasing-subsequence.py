
# MAX SUM INCREASING SUBSEQUENCE

# O(N!) time, O(N) space
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    return calculateMaxSum(float('-inf'), array, [], 0)

def calculateMaxSum(totalSum, currentArray, sumArray, index):
	if index >= len(currentArray):
		return [totalSum, sumArray]
	
	lastElement = sumArray[-1] if sumArray else float('-inf')
	if currentArray[index] <= lastElement:
		return calculateMaxSum(totalSum, currentArray, sumArray, index+1)
	else:
		currentElement = currentArray[index]
		if totalSum == float('-inf'):
			maxSumWithCurrentElement = calculateMaxSum(currentElement, currentArray, sumArray + [currentElement], index+1)
		else:
			maxSumWithCurrentElement = calculateMaxSum(totalSum + currentElement, currentArray, sumArray + [currentElement], index+1)
		maxSumWithoutCurrentElement = calculateMaxSum(totalSum, currentArray, sumArray, index+1)
		
		return maxSumWithCurrentElement if maxSumWithCurrentElement[0] > maxSumWithoutCurrentElement[0] else maxSumWithoutCurrentElement
	

# O(N^2) time, O(N) space
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    sequences = [None for x in array]
	sums = [num for num in array]
	maxSumIndex = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(0, i):
			otherNum = array[j]
			if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
				sums[i] = sums[j] + currentNum
				sequences[i] = j
		if sums[i] >= sums[maxSumIndex]:
			maxSumIndex = i
	return [sums[maxSumIndex], buildSequence(array, sequences, maxSumIndex)]

def buildSequence(array, sequences, currentIndex):
	sequence = []
	while currentIndex is not None:
		sequence.append(array[currentIndex])
		currentIndex = sequences[currentIndex]
	return list(reversed(sequence))

