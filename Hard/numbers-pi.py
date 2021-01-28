
# NUMBERS IN PI

# O(N^3 + M) time and O(N + M) space
def numbersInPi(pi, numbers):
    # Write your code here.
    number = {}
	for num in numbers:
		number[num] = True
	
	return findMinSpaces(pi, 0, number, 0)
	
def findMinSpaces(pi, index, number, spaceCount):
	if index >= len(pi):
		print(spaceCount)
		return spaceCount - 1
	
	minSpaces = float('inf')
	for i in range(index, len(pi)):
		if pi[index:i+1] in number:
			spaces = findMinSpaces(pi, i+1, number, spaceCount + 1)
			if spaces != -1:
				minSpaces = min(minSpaces, spaces)
				
	return -1 if minSpaces == float('inf') else minSpaces

# O(N^3 + M) time and O(N + M) space
def numbersInPi(pi, numbers):
    # Write your code here.
    number = {}
	for num in numbers:
		number[num] = True
	cache = {}
	space = findMinSpaces(pi, 0, number, cache)
	return -1 if cache[0] == float('inf') else cache[0]
	
def findMinSpaces(pi, index, number, knownSpaces):
	print("INDEX", index)
	if index == len(pi):
		return -1
	
	if index in knownSpaces:
		return knownSpaces[index]
	
	minSpaces = float('inf')
	for i in range(index, len(pi)):
		if pi[index:i+1] in number:
			print("MATCH", pi[index:i+1])
			spaces = findMinSpaces(pi, i+1, number, knownSpaces)
			minSpaces = min(minSpaces, spaces+1)
	knownSpaces[index] = minSpaces
	print(knownSpaces[index], index)
	return knownSpaces[index]
