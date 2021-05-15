
# GLOB MATCHING

# RECURSIVE SOLUTION. NOT OPTIMAL> BAD APPROACH SINCE IT TAKES INTO ACCOUNT NUMEROUS TEST CASES AND MANIPULATES THE SOLUTION
def globMatching(fileName, pattern):
    # Write your code here.
	if len(pattern) > 0 and pattern[0] == "*":
		pos = findNextCharacter(pattern, 0)
		if pos == -1:
			print("returning at beginning")
			return True
    return matchGlob(fileName, pattern, 0, 0)

def matchGlob(filename, pattern, index1, index2):
	if index1 == len(filename) and index2 == len(pattern):
		return True
	
	if index1 == len(filename) or index2 == len(pattern):
		return False
	print("checking", filename[index1], pattern[index2])
	
	if pattern[index2] not in ["?", "*"] and pattern[index2] != filename[index1]:
		return False
	
	if pattern[index2] == "?":
		return matchGlob(filename, pattern, index1 + 1, index2 + 1)
	
	if pattern[index2] != "*":
		return matchGlob(filename, pattern, index1 + 1, index2 + 1)
	
	nextCharPos = findNextCharacter(pattern, index2)
	if nextCharPos == -1:
		print("returning")
		return True
	check = False
	for i in range(index1, len(filename)):
		print("erererchecking", filename[i], pattern[nextCharPos])
		check = matchGlob(filename, pattern, i, nextCharPos)
		if check:
			return True
		
	return False

def findNextCharacter(pattern, index):
	for i in range(index, len(pattern)):
		if pattern[i] == "*":
			continue
		else:
			return i
	return -1

# O(n * m) time and space
def globMatching(fileName, pattern):
    # Write your code here.
	match = [[False for _ in range(len(pattern) + 1)] for _ in range(len(fileName) + 1)]
	match[0][0] = True
	for i in range(1, len(fileName) + 1):
		match[i][0] = False
		
	for row in range(len(fileName) + 1):
		for col in range(1, len(pattern) + 1):
			if row == 0:
				if pattern[col - 1] == "*":
					match[row][col] = match[row][col - 1]
				continue
			
			if pattern[col - 1] == "*":
				match[row][col] = match[row - 1][col - 1] or match[row][col - 1] or match[row - 1][col]
			elif pattern[col - 1] == "?":
				match[row][col] = match[row - 1][col - 1]
			else:
				match[row][col] = match[row - 1][col - 1] and fileName[row - 1] == pattern[col - 1]
	print(match)
	return match[-1][-1]
	