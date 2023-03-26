
# SAME BSTS

# O(N^2) time and space
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
	if len(arrayOne) != len(arrayTwo):
		return False
	
	if len(arrayOne) == 0:
		return True
	
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	leftSubtreeFirst = [num for num in arrayOne[1:] if num < arrayOne[0]]
	rightSubtreeFirst = [num for num in arrayOne[1:] if num >= arrayOne[0]]
	leftSubtreeSecond = [num for num in arrayTwo[1:] if num < arrayTwo[0]]
	rightSubtreeSecond = [num for num in arrayTwo[1:] if num >= arrayTwo[0]]
    
	return sameBsts(leftSubtreeFirst, leftSubtreeSecond) and sameBsts(rightSubtreeFirst, rightSubtreeSecond)


# O(N^2) time and O(d) space
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))

def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
	if rootIdxOne == -1 or rootIdxTwo == -1:
		return rootIdxOne == rootIdxTwo
	
	if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
		return False
	
	leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
	leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
	rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
	rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)

	currentValue = arrayOne[rootIdxOne]
	leftAreSame = areSameBsts(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
	rightAreSame = areSameBsts(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)
	
	return leftAreSame and rightAreSame

def getIdxOfFirstSmaller(array, startingIdx, minVal):
	for i in range(startingIdx + 1, len(array)):
		if array[i] < array[startingIdx] and array[i] >= minVal:
			return i
		
	return -1

def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
	for i in range(startingIdx + 1, len(array)):
		if array[i] >= array[startingIdx] and array[i] < maxVal:
			return i
		
	return -1