
# SPIRAL TRAVERSE

# O(NM) tie and space
def spiralTraverse(array):
    # Write your code here.
	if len(array) == 0 or len(array[0]) == 0:
		return []
    result = []
	rowUp = 0
	rowDown = len(array) - 1
	colFront = 0
	colBack = len(array[0]) - 1
	
	while rowUp <= rowDown and colFront <= colBack:
		traverseBoundary(array, rowUp, rowDown, colFront, colBack, result)
		rowUp += 1
		rowDown -= 1
		colFront += 1
		colBack -= 1
	return result

def traverseBoundary(array, rowUp, rowDown, colFront, colBack, result):
	for i in range(colFront, colBack+1):
		result.append(array[rowUp][i])
		
	for i in range(rowUp+1, rowDown+1):
		result.append(array[i][colBack])
	
	if rowUp != rowDown:
		for i in reversed(range(colFront, colBack)):
			result.append(array[rowDown][i])
	
	if colFront != colBack:
		for i in reversed(range(rowUp+1, rowDown)):
			result.append(array[i][colFront])
	