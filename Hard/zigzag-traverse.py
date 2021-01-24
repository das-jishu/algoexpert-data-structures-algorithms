
# ZIGZAG TRAVERSE

# O(NM) time and space
def zigzagTraverse(array):
    # Write your code here.
	totalRows, totalColumns = len(array), len(array[0])
    zigzagTraverse = []
	row, col = 0, 0
	direction = 'down'
	
	while row in range(totalRows) and col in range(totalColumns):
		
		while row in range(totalRows) and col in range(totalColumns):
			zigzagTraverse.append(array[row][col])
			print("currently in ", row, col)
			row = row - 1 if direction == 'up' else row + 1
			col = col + 1 if direction == 'up' else col - 1
			
		if direction == 'up':
			if col < totalColumns:
				row = 0
			else:
				col = totalColumns - 1
				row += 2
		else:
			if row < totalRows:
				col = 0
			else:
				row = totalRows - 1
				col += 2
		nextStart = (row, col)
		print(nextStart)
		direction = 'down' if direction == 'up' else 'up'
		
	return zigzagTraverse