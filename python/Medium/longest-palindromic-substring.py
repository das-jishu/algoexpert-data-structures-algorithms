
# O(N^2) time and O(N) space
def longestPalindromicSubstring(string):
    # Write your code here.
    longestPalindrome = ""
	if len(string) < 2:
		return string
	
	i = 0
	while i < len(string) - 1:
		palinSingle = getLongestPalindrome(string, i, i)
		longestPalindrome = palinSingle if len(palinSingle) > len(longestPalindrome) else longestPalindrome
		if string[i] == string[i+1]:
			palinDouble = getLongestPalindrome(string, i, i+1)
			longestPalindrome = palinDouble if len(palinDouble) > len(longestPalindrome) else longestPalindrome
		i += 1
		
	return longestPalindrome

def getLongestPalindrome(string, i, j):
	palin = string[i] if i == j else string[i] * 2
	i -= 1
	j += 1
	while i >= 0 and j < len(string) and string[i] == string[j]:
		palin = string[i] + palin + string[j]
		i -= 1
		j += 1
	return palin