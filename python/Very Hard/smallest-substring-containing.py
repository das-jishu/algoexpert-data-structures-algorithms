
# SMALLEST SUBSTRING CONTAINING

# O(b + s) time and space
def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    targetCharCounts = getCharCounts(smallString)
	substringBounds = getSubstringBounds(bigString, targetCharCounts)
	return getStringFromBounds(bigString, substringBounds)

def getCharCounts(string):
	charCounts = {}
	for char in string:
		increaseCharCount(char, charCounts)
	return charCounts

def getSubstringBounds(string, targetCharCounts):
	substringBounds = [0, float("inf")]
	substringCharCounts = {}
	numUniqueChars = len(targetCharCounts.keys())
	numUniqueCharsDone = 0
	leftIdx = 0
	rightIdx = 0
	
	while rightIdx < len(string):
		rightChar = string[rightIdx]
		if rightChar not in targetCharCounts:
			rightIdx += 1
			continue
		increaseCharCount(rightChar, substringCharCounts)
		if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
			numUniqueCharsDone += 1
			
		while numUniqueCharsDone == numUniqueChars and leftIdx <= rightIdx:
			substringBounds = getCloserBounds(leftIdx, rightIdx, substringBounds[0], substringBounds[1])
			leftChar = string[leftIdx]
			if leftChar not in targetCharCounts:
				leftIdx += 1
				continue
			if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
				numUniqueCharsDone -= 1
			decreaseCharCount(leftChar, substringCharCounts)
			leftIdx += 1
		rightIdx += 1
	return substringBounds

def getCloserBounds(idx1, idx2, idx3, idx4):
	return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]

def getStringFromBounds(string, bounds):
	start, end = bounds
	if end == float("inf"):
		return ""
	return string[start : end + 1]

def increaseCharCount(char, charCounts):
	if char not in charCounts:
		charCounts[char] = 0
	charCounts[char] += 1
	
def decreaseCharCount(char, charCounts):
	charCounts[char] -= 1
