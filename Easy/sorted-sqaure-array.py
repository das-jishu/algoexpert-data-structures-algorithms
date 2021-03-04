
# SORTED SQUARE ARRAY

# O(NlogN) time and O(N) space
def sortedSquaredArray(array):
    # Write your code here.
	squares = []
    for number in array:
		squares.append(number ** 2)
	return sorted(squares)

# O(N) time and space
def sortedSquaredArray(array):
    # Write your code here.
    squares = []
	leftIndex = 0
	rightIndex = len(array) - 1
	while leftIndex <= rightIndex:
		leftValue = abs(array[leftIndex])
		rightValue = abs(array[rightIndex])
		if leftValue > rightValue:
			squares.append(leftValue ** 2)
			leftIndex += 1
		else:
			squares.append(rightValue ** 2)
			rightIndex -= 1
	return list(reversed(squares))