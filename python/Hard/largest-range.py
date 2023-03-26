
# O(N) time and space
def largestRange(array):
    # Write your code here.
    values = {}
	for number in array:
		values[number] = False

	largest = [array[0], array[0]]
	for number in array:
		if values[number]:
			continue
		moveRight = number
		while moveRight in values:
			values[moveRight] = True
			moveRight += 1
		moveLeft = number
		while moveLeft in values:
			values[moveLeft] = True
			moveLeft -= 1
		if (largest[1] - largest[0]) < (moveRight - moveLeft - 2):
			largest = [moveLeft + 1, moveRight - 1]
			
	return largest
			
		
