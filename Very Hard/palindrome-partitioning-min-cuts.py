
# PALINDROME PARTITIONING MIN CUTS

# O(N^2) time and space
def palindromePartitioningMinCuts(string):
    # Write your code here.
    palindromes = [[False for _ in string] for __ in string]
	for i in range(len(string)):
		palindromes[i][i] = True
		
	for length in range(2, len(string) + 1):
		for start in range(0, len(string) - length + 1):
			end = start + length - 1
			if length == 2:
				palindromes[start][end] = string[start] == string[end]
			else:
				palindromes[start][end] = palindromes[start + 1][end - 1] and string[start] == string[end]
	cuts = [float("inf") for _ in string]
	for i in range(len(string)):
		if palindromes[0][i]:
			cuts[i] = 0
		else:
			cuts[i] = cuts[i-1] + 1
			for j in range(1, i):
				if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
					cuts[i] = cuts[j - 1] + 1
	return cuts[-1]