
# SEARCH IN SORTED MATRIX

# O(N + M) time and O(1) space
def searchInSortedMatrix(matrix, target):
    # Write your code here.
    i = 0
	j = len(matrix[0]) - 1
	
	while i < len(matrix) and j >= 0:
		if matrix[i][j] == target:
			return [i, j]
		if target < matrix[i][j]:
			j -= 1
		else:
			i += 1
			
	return [-1, -1]
