
# SPIN RINGS

# O(N^2) time and O(1) space. N is the size of the input array.
def spinRings(array):
    # Write your code here.
    m = len(array)
	
	startRow, endRow, startCol, endCol = 0, m - 1, 0, m - 1
	
	# If the innermost set has only one ring, we don't need to iterate
	# through it again, since moving it clockwise will repeat the same thing.
	# Hence, condition says < and not <= below.
	while startRow < endRow:
		element = array[startRow][startCol]
		
		for col in range(startCol + 1, endCol + 1):
			next = array[startRow][col]
			array[startRow][col] = element
			element = next
		
		for row in range(startRow + 1, endRow + 1):
			next = array[row][endCol]
			array[row][endCol] = element
			element = next
		
		for col in reversed(range(startCol, endCol)):
			next = array[endRow][col]
			array[endRow][col] = element
			element = next
		
		for row in reversed(range(startRow, endRow)):
			next = array[row][startCol]
			array[row][startCol] = element
			element = next
			
		startRow += 1
		startCol += 1
		endRow -= 1
		endCol -= 1
		
	return array
