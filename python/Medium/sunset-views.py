
# SUNSET VIEWS

# O(N) time and space
def sunsetViews(buildings, direction):
    # Write your code here.
    result = []
	
	step = 1 if direction == "EAST" else -1
	start = 0 if direction == "EAST" else len(buildings) - 1
	
	index = start
	while index >= 0 and index < len(buildings):
		height = buildings[index]
		
		while len(result) > 0 and buildings[result[-1]] <= height:
			result.pop()
			
		result.append(index)
		index += step
		
	return result if direction == "EAST" else result[::-1]

# O(N) time and space
def sunsetViews(buildings, direction):
    # Write your code here.
	result = []
	
	step = 1 if direction == "WEST" else -1
	start = 0 if direction == "WEST" else len(buildings) - 1
	
	index = start
	currentMax = float('-inf')
	while index >= 0 and index < len(buildings):
		if buildings[index] > currentMax:
			result.append(index)
			currentMax = buildings[index]
		
		index += step
		
	return result if direction == "WEST" else result[::-1]