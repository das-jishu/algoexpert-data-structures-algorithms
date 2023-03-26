
# SINGLE CYCLE CHECK

# O(N) time and O(1) space
def hasSingleCycle(array):
    # Write your code here.
	i = 0
    while array[i] != None:
		jump = array[i]
		array[i] = None
		if jump >= 0:
			i = (jump + i) % len(array)
		else:
			jump = abs(jump) % len(array)
			if i - jump < 0:
				i = len(array) + (i - jump)
			else:
				i -= jump
	
	if i != 0:
		return False
	print(array)
	for x in array:
		if x != None:
			return False
		
	return True
		
# O(N) time and O(1) space
def hasSingleCycle(array):
    # Write your code here.
    visited = 0
	currentIndex = 0
	while visited < len(array):
		if visited > 0 and currentIndex == 0:
			return False
		visited += 1
		currentIndex = getNextIndex(currentIndex, array)
	return currentIndex == 0

def getNextIndex(currentIndex, array):
	jump = array[currentIndex]
	nextIndex = (currentIndex + jump) % len(array)
	return nextIndex if nextIndex >= 0 else nextIndex + len(array)
