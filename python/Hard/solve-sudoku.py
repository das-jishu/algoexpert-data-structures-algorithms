
# SOLVE SUDOKU

# O(1) time and space
def solveSudoku(board):
    # Write your code here.
    solvePartialSudoku(0, 0, board)
	return board

def solvePartialSudoku(row, col, board):
	currentRow = row
	currentCol = col
	
	if currentCol == len(board[currentRow]):
		currentRow += 1
		currentCol = 0
		if currentRow == len(board):
			return True
		
	if board[currentRow][currentCol] == 0:
		return tryDigitsAtPosition(currentRow, currentCol, board)
	
	return solvePartialSudoku(currentRow, currentCol + 1, board)

def tryDigitsAtPosition(row, col, board):
	for digit in range(1, 10):
		if isVAlidAtPosition(digit, row, col, board):
			board[row][col] = digit
			if solvePartialSudoku(row, col + 1, board):
				return True
			
	board[row][col] = 0
	return False

def isVAlidAtPosition(value, row, col, board):
	rowIsValid = value not in board[row]
	columnIsValid = value not in map(lambda r: r[col], board)
	
	if not rowIsValid or not columnIsValid:
		return False
	
	subgridRowStart = (row // 3) * 3
	subgridColStart = (col // 3) * 3
	for rowIdx in range(3):
		for colIdx in range(3):
			rowToCheck = subgridRowStart + rowIdx
			colToCheck = subgridColStart + colIdx
			existingValue = board[rowToCheck][colToCheck]
			
			if existingValue == value:
				return False
			
	return True
