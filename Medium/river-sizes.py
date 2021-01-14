
# RIVER SIZES

# O(WH) time and space
def riverSizes(matrix):
    # Write your code here.
    sizesOfRivers = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 1:
				sizesOfRivers.append(calculateSize(matrix, i, j))
	return sizesOfRivers

def calculateSize(matrix, i, j):
	if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]) or matrix[i][j] in (0, 'K'):
		return 0
	
	matrix[i][j] = 'K'
	return 1 + calculateSize(matrix, i+1, j) + calculateSize(matrix, i-1, j) + calculateSize(matrix, i, j+1) + calculateSize(matrix, i, j-1)

# O(WH) time and space
def riverSizes(matrix):
    # Write your code here.
    riverSizes = []
	visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if visited[i][j]:
				continue
			size = traverse(matrix, i, j, visited)
			if size > 0:
				riverSizes.append(size)
	return riverSizes

def traverse(matrix, i, j, visited):
	currentRiverSize = 0
	stack = [[i,j]]
	while stack:
		node = stack.pop()
		m = node[0]
		n = node[1]
		if visited[m][n]:
			continue
		visited[m][n] = True
		if matrix[m][n] == 0:
			continue
		currentRiverSize += 1
		unvisited = getUnvisited(matrix, m, n, visited)
		for x in unvisited:
			stack.append(x)
	return currentRiverSize

def getUnvisited(matrix, i, j, visited):
	unvisitedNodes = []
	if i > 0 and not visited[i-1][j]:
		unvisitedNodes.append([i-1, j])
	if i < len(matrix) - 1 and not visited[i+1][j]:
		unvisitedNodes.append([i+1, j])
	if j > 0 and not visited[i][j-1]:
		unvisitedNodes.append([i,j-1])
	if j < len(matrix[0]) - 1 and not visited[i][j+1]:
		unvisitedNodes.append([i,j+1])
	return unvisitedNodes