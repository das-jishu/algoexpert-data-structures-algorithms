
# MINIMUM PASSES OF MATRIX

# O(W * H) time and space
def minimumPassesOfMatrix(matrix):
    # Write your code here.
    passes = convertNegatives(matrix)
	return passes - 1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
	nextPassQueue = getAllPositivePositions(matrix)
	
	passes = 0
	while len(nextPassQueue) > 0:
		currentPassQueue = nextPassQueue
		nextPassQueue = []
		
		while len(currentPassQueue) > 0:
			row, column = currentPassQueue.pop(0)
			adjacentPositions = getAdjacentPositions(row, column, matrix)
			for position in adjacentPositions:
				r, c = position
				value = matrix[r][c]
				if value < 0:
					matrix[r][c] *= -1
					nextPassQueue.append([r, c])

		passes += 1
	return passes

def getAllPositivePositions(matrix):
	positives = []
	
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			value = matrix[row][col]
			if value > 0:
				positives.append([row, col])
				
	return positives

def getAdjacentPositions(row, col, matrix):
	adjacents = []
	
	if row > 0:
		adjacents.append([row - 1, col])
	if row < len(matrix) - 1:
		adjacents.append([row + 1, col])
	if col > 0:
		adjacents.append([row, col - 1])
	if col < len(matrix[0]) - 1:
		adjacents.append([row, col + 1])
		
	return adjacents

def containsNegative(matrix):
	for row in matrix:
		for value in row:
			if value < 0:
				return True
	return False