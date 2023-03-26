
# LONGEST SUBSTRING WITHOUT DUPLICATION

# O(N) time, O(min(n, a)) space -> a is the number of unique characters in string
def longestSubstringWithoutDuplication(string):
    # Write your code here.
    lastSeenChar = {}
	longest = [0, 1]
	startIdx = 0
	for i, char in enumerate(string):
		if char in lastSeenChar:
			startIdx = max(startIdx, lastSeenChar[char] + 1)
		if longest[1] - longest[0] < i + 1 - startIdx:
			longest = [startIdx, i + 1]
		lastSeenChar[char] = i
	return string[longest[0] : longest[1]]
	
