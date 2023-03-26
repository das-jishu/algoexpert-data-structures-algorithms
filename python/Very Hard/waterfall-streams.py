
# WATERFALL STREAMS

# O(W^2*H) time, O(W) space -> W: Width, H: Height
def waterfallStreams(array, source):
    # Write your code here.
	height, width = len(array), len(array[0])
    previousRow = [0 for _ in range(width)]
	nextRow = [0 for _ in range(width)]
	
	currentRowNumber = 0
	previousRow[source] = 100
	
	while currentRowNumber < height - 1:
		nextRow = [0 for _ in range(width)]
		# getting positions where water is present and will fall down
		for i in range(width):
			if array[currentRowNumber][i] == 0 and previousRow[i] > 0:
				# for each position, checking if water will split or go down
				position = i
				# no block so goes down
				if array[currentRowNumber + 1][position] == 0:
					nextRow[position] += previousRow[position]
					continue

				amountOfWater = previousRow[position] / 2
				current = position
				while current > 0:
					isMovePossible = array[currentRowNumber + 1][current] == 1 and array[currentRowNumber][current - 1] != 1
					if isMovePossible:
						nextRow[current - 1] += amountOfWater
					else:
						break
					current -= 1

				current = position
				while current < width - 1:
					isMovePossible = array[currentRowNumber + 1][current] == 1 and array[currentRowNumber][current + 1] != 1
					if isMovePossible:
						nextRow[current + 1] += amountOfWater
					else:
						break
					current += 1
				
		previousRow = nextRow
		currentRowNumber += 1
		
	return nextRow
