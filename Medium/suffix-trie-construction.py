
# SUFFIX TRIE CONSTRUCTION

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

	# O(N^2) time and space
    def populateSuffixTrieFrom(self, string):
        # Write your code here.
		i = len(string) - 1
		while i >= 0:
			currentPosition = self.root
			for j in range(i, len(string)):
				if string[j] not in currentPosition:
					currentPosition[string[j]] = {}
				currentPosition = currentPosition[string[j]]
			currentPosition[self.endSymbol] = True
			i -= 1

	# O(M) time and O(1) space -> M - length of search word
    def contains(self, string):
        # Write your code here.
        i = 0
		currentPosition = self.root
		while i < len(string):
			if string[i] not in currentPosition:
				return False
			currentPosition = currentPosition[string[i]]
			i += 1
			
		return self.endSymbol in currentPosition
