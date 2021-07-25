
# GLOB MATCHING

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
	