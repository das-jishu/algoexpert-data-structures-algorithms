
# LONGEST INCREASING MATRIX PATH

# O(M * N) time, O(M * N) space, M -> number of rows in input matrix
# N -> number of columns in input matrix
def longestIncreasingMatrixPath(matrix):
    # Write your code here.
    maxLength = 0
	m, n = len(matrix), len(matrix[0])
	cache = [[None for i in range(n)] for j in range(m)]
	
	for i in range(m):
		for j in range(n):
			length = findLongest(matrix, i, j, cache)
			maxLength = max(maxLength, length)
	
	return maxLength

def findLongest(matrix, row, col, cache):
	if cache[row][col] != None:
		return cache[row][col]
	
	num = matrix[row][col]
	matrix[row][col] = None
	
	neighbors = getNeighbors(matrix, row, col)
	maximum = float("-inf")
	for i, j in neighbors:
		if matrix[i][j] == None or matrix[i][j] <= num:
			continue
		getMaxLength = findLongest(matrix, i, j, cache)
		maximum = max(maximum, 1 + getMaxLength)
		
	matrix[row][col] = num
	cache[row][col] = maximum if maximum != float("-inf") else 1
	
	return cache[row][col]
	
def getNeighbors(matrix, row, col):
	neighbors = []
	
	if row != 0:
		neighbors.append([row - 1, col])
	if row != len(matrix) - 1:
		neighbors.append([row + 1, col])
	if col != 0:
		neighbors.append([row, col - 1])
	if col != len(matrix[0]) - 1:
		neighbors.append([row, col + 1])
		
	return neighbors