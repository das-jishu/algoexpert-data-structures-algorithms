
# LONGEST COMMON SUBSEQUENCE

# O(nm*min(n,m)) time, space
def longestCommonSubsequence(str1, str2):
    # Write your code here.
    commonSequence = [["" for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
	
	for i in range(1, len(str1) + 1):
		for j in range(1, len(str2) + 1):
			if str1[i-1] == str2[j-1]:
				commonSequence[i][j] = commonSequence[i-1][j-1] + str1[i-1]	
			else:
				currentSubstring = commonSequence[i][j-1]
				previousSubstring = commonSequence[i-1][j]
				commonSequence[i][j] = max(currentSubstring, previousSubstring, key=len)
	
	return list(commonSequence[-1][-1])
				
# O(nm*min(n,m)) time, O(min(n,m)^2) space
def longestCommonSubsequence(str1, str2):
    # Write your code here.
    small = min(str1, str2, key=len)
	big = str1 if small == str2 else str2
	evenRow = [[] for _ in range(len(small) + 1)]
	oddRow = [[] for _ in range(len(small) + 1)]
	
	for i in range(1, len(big) + 1):
		for j in range(1, len(small) + 1):
			if i % 2 != 0:
				if big[i-1] == small[j-1]:
					oddRow[j] = evenRow[j-1] + [big[i-1]]	
				else:
					currentSubstring = oddRow[j-1]
					previousSubstring = evenRow[j]
					oddRow[j] = max(currentSubstring, previousSubstring, key=len)
			
			else:
				if big[i-1] == small[j-1]:
					evenRow[j] = oddRow[j-1] + [big[i-1]]	
				else:
					currentSubstring = evenRow[j-1]
					previousSubstring = oddRow[j]
					evenRow[j] = max(currentSubstring, previousSubstring, key=len)
					
	return evenRow[-1] if len(big) % 2 == 0 else oddRow[-1]
				
# O(NM) time and space
def longestCommonSubsequence(str1, str2):
    # Write your code here.
    lcs = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i-1] == str1[j-1]:
				lcs[i][j] = [str2[i-1], lcs[i-1][j-1][1] + 1, i-1, j-1]
			else:
				if lcs[i-1][j][1] > lcs[i][j-1][1]:
					lcs[i][j] = [None, lcs[i-1][j][1], i - 1, j]
				else:
					lcs[i][j] = [None, lcs[i][j-1][1], i, j-1]
	return buildSequence(lcs)

def buildSequence(lcs):
	sequence = []
	i = len(lcs) - 1
	j = len(lcs[0]) - 1
	while i != 0 and j != 0:
		currentEntry = lcs[i][j]
		if currentEntry[0] is not None:
			sequence.append(currentEntry[0])
		i = currentEntry[2]
		j = currentEntry[3]
	return list(reversed(sequence))
