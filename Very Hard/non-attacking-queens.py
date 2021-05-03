
# NON-ATTACKING QUEENS

# LOWER BOUND: O(N!) time and O(N) space
def nonAttackingQueens(n):
    # Write your code here.
    columns = [0] * n
	return getTotalPlacements(0, columns, n)

def getTotalPlacements(row, columns, board):
	if board == row:
		return 1
	
	totalPlacements = 0
	for col in range(board):
		if isNonAttacking(row, col, columns):
			columns[row] = col
			totalPlacements += getTotalPlacements(row + 1, columns, board)
			
	return totalPlacements

def isNonAttacking(row, col, columns):
	for previous in range(row):
		if columns[previous] == col:
			return False
		if abs(columns[previous] - col) == row - previous:
			return False
	
	return True
