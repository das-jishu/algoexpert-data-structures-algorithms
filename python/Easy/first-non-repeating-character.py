
# FIRST NON REPEATING CHARACTER

# O(N) time and O(1) space
def firstNonRepeatingCharacter(string):
    # Write your code here.
    counts = {}
	for index, char in enumerate(string):
		if char in counts:
			counts[char][1] += 1
		else:
			counts[char] = [index, 1]
	
	minIndex = float("inf")
	for char in counts:
		if counts[char][1] == 1:
			minIndex = min(minIndex, counts[char][0])
	
	return -1 if minIndex == float("inf") else minIndex