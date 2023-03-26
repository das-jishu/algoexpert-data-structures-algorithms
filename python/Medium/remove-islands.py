
# REMOVE ISLANDS

# O(wh) time and space
def removeIslands(matrix):
    # Write your code here.
    m = len(matrix)
	n = len(matrix[0])
	
	for i in range(n):
		if matrix[0][i] == 1:
			markAllBorderBlacks(matrix, 0, i)
			
	for i in range(m):
		if matrix[i][0] == 1:
			markAllBorderBlacks(matrix, i, 0)
			
	for i in range(n):
		if matrix[m-1][i] == 1:
			markAllBorderBlacks(matrix, m-1, i)
			
	for i in range(m):
		if matrix[i][n-1] == 1:
			markAllBorderBlacks(matrix, i, n-1)
			
	removeAllIslands(matrix)
	return matrix

def markAllBorderBlacks(matrix, i, j):
	if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]) or matrix[i][j] in [0, 'K']:
		return
	
	matrix[i][j] = 'K'
	markAllBorderBlacks(matrix, i+1, j)
	markAllBorderBlacks(matrix, i, j+1)
	markAllBorderBlacks(matrix, i-1, j)
	markAllBorderBlacks(matrix, i, j-1)
	
def removeAllIslands(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				matrix[i][j] = 0
			if matrix[i][j] == 'K':
				matrix[i][j] = 1
				

# O(wh) time and space
def removeIslands(matrix):
    # Write your code here.
    for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			isRowBorder = row == 0 or row == len(matrix) - 1
			isColBorder = col == 0 or col == len(matrix[0]) - 1
			isBorder = isRowBorder or isColBorder
			if not isBorder:
				continue
			print(matrix)
			if matrix[row][col] == 1:
				changeConnectedBlacks(matrix, row, col)
				
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				matrix[i][j] = 0
			if matrix[i][j] == -1:
				matrix[i][j] = 1
	
	return matrix
				
def changeConnectedBlacks(matrix, i, j):
	stack = [[i, j]]
	while len(stack) > 0:
		temp = stack.pop()
		i = temp[0]
		j = temp[1]
		
		if matrix[i][j] == 0 or matrix[i][j] == -1:
			continue
			
		matrix[i][j] = -1
		unvisitedNeighbors = getAllNeighbors(matrix, i, j)
		for neighbor in unvisitedNeighbors:
			stack.append(neighbor)
			
def getAllNeighbors(matrix, i, j):
	neighbors = []
	
	if not i == 0:
		neighbors.append([i-1, j])
	if not i == len(matrix) - 1:
		neighbors.append([i+1, j])
	if not j == 0:
		neighbors.append([i, j-1])
	if not j == len(matrix[0]) - 1:
		neighbors.append([i, j+1])
		
	return neighbors
				
