
# SQUARE OF ZEROES

# O(N^4) time and O(1) space
def squareOfZeroes(matrix):
    # Write your code here.
    n = len(matrix)
	for topRow in range(n):
		for leftCol in range(n):
			squareLength = 2
			while squareLength <= n - leftCol and squareLength <= n - topRow:
				bottomRow = topRow + squareLength - 1
				rightCol = leftCol + squareLength - 1
				if isSquareOfZeroes(matrix, topRow, leftCol, bottomRow, rightCol):
					return True
				squareLength += 1
	return False

def isSquareOfZeroes(matrix, r1, c1, r2, c2):
	for row in range(r1, r2 + 1):
		if matrix[row][c1] != 0 or matrix[row][c2] != 0:
			return False
	for col in range(c1, c2 + 1):
		if matrix[r1][col] != 0 or matrix[r2][col] != 0:
			return False
	return True
		

# O(N^3) time and space
def squareOfZeroes(matrix):
    # Write your code here.
    infoMatrix = preComputeNumOfZeroes(matrix)
	lastIdx = len(matrix) - 1
	return hasSquareOfZeroes(infoMatrix, 0, 0, lastIdx, lastIdx, {})


def hasSquareOfZeroes(infoMatrix, r1, c1, r2, c2, cache):
	if r1 >= r2 or c1 >= c2:
		return False
	
	key = str(r1) + "-" + str(c1) + "-" + str(r2) + "-" + str(c2)
	if key in cache:
		return cache[key]
	
	cache[key] = (
		isSquareOfZeroes(infoMatrix, r1, c1, r2, c2)
		or hasSquareOfZeroes(infoMatrix, r1 + 1, c1 + 1, r2 - 1, c2 - 1, cache)
		or hasSquareOfZeroes(infoMatrix, r1, c1 + 1, r2 - 1, c2, cache)
		or hasSquareOfZeroes(infoMatrix, r1 + 1, c1, r2, c2 - 1, cache)
		or hasSquareOfZeroes(infoMatrix, r1 + 1, c1 + 1, r2, c2, cache)
		or hasSquareOfZeroes(infoMatrix, r1, c1, r2 - 1, c2 - 1, cache)
	)
	
	return cache[key]

def isSquareOfZeroes(infoMatrix, r1, c1, r2, c2):
	squareLength = c2 - c1 + 1
	hasTopBorder = infoMatrix[r1][c1]["numZeroesRight"] >= squareLength
	hasLeftBorder = infoMatrix[r1][c1]["numZeroesBelow"] >= squareLength
	hasBottomBorder = infoMatrix[r2][c1]["numZeroesRight"] >= squareLength
	hasRightBorder = infoMatrix[r1][c2]["numZeroesBelow"] >= squareLength
	return hasTopBorder and hasLeftBorder and hasBottomBorder and hasRightBorder

def preComputeNumOfZeroes(matrix):
	infoMatrix = [[x for x in row] for row in matrix]	
	
	n = len(matrix)
	for row in range(n):
		for col in range(n):
			numZeroes = 1 if matrix[row][col] == 0 else 0
			infoMatrix[row][col] = {
				"numZeroesBelow": numZeroes,
				"numZeroesRight": numZeroes,
			}
	
	lastIdx = len(matrix) - 1
	for row in reversed(range(n)):
		for col in reversed(range(n)):
			if matrix[row][col] == 1:
				continue
			if row < lastIdx:
				infoMatrix[row][col]["numZeroesBelow"] += infoMatrix[row + 1][col]["numZeroesBelow"]
			if col < lastIdx:
				infoMatrix[row][col]["numZeroesRight"] += infoMatrix[row][col + 1]["numZeroesRight"]
				
	return infoMatrix


# O(N^3) time and O(N^2) space
def squareOfZeroes(matrix):
    # Write your code here
	infoMatrix = preComputeNumOfZeroes(matrix)
    n = len(matrix)
	for topRow in range(n):
		for leftCol in range(n):
			squareLength = 2
			while squareLength <= n - leftCol and squareLength <= n - topRow:
				bottomRow = topRow + squareLength - 1
				rightCol = leftCol + squareLength - 1
				if isSquareOfZeroes(infoMatrix, topRow, leftCol, bottomRow, rightCol):
					return True
				squareLength += 1
	return False
    
def isSquareOfZeroes(infoMatrix, r1, c1, r2, c2):
	squareLength = c2 - c1 + 1
	hasTopBorder = infoMatrix[r1][c1]["numZeroesRight"] >= squareLength
	hasLeftBorder = infoMatrix[r1][c1]["numZeroesBelow"] >= squareLength
	hasBottomBorder = infoMatrix[r2][c1]["numZeroesRight"] >= squareLength
	hasRightBorder = infoMatrix[r1][c2]["numZeroesBelow"] >= squareLength
	return hasTopBorder and hasLeftBorder and hasBottomBorder and hasRightBorder

def preComputeNumOfZeroes(matrix):
	infoMatrix = [[x for x in row] for row in matrix]
	
	n = len(matrix)
	for row in range(n):
		for col in range(n):
			numZeroes = 1 if matrix[row][col] == 0 else 0
			infoMatrix[row][col] = {
				"numZeroesBelow": numZeroes,
				"numZeroesRight": numZeroes,
			}
	
	lastIdx = len(matrix) - 1
	for row in reversed(range(n)):
		for col in reversed(range(n)):
			if matrix[row][col] == 1:
				continue
			if row < lastIdx:
				infoMatrix[row][col]["numZeroesBelow"] += infoMatrix[row + 1][col]["numZeroesBelow"]
			if col < lastIdx:
				infoMatrix[row][col]["numZeroesRight"] += infoMatrix[row][col + 1]["numZeroesRight"]
				
	return infoMatrix