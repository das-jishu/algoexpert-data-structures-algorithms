
# SPECIAL STRINGS

# O(N * M) time and O(N * M) space
def specialStrings(strings):
    # Write your code here.
    trie = Trie()
	for string in strings:
		trie.buildTrie(string)
		
	specials = []
	for string in strings:
		if checkSpecial(string, trie.root, 0, 0, trie):
			specials.append(string)
			
	return specials
		
def checkSpecial(string, node, index, count, trie):
	letter = string[index]
	if letter not in node:
		return False
	
	if index == len(string) - 1:
		return trie.endSymbol in node[letter] and count > 0
	
	if trie.endSymbol in node[letter]:
		remainingSpecial = checkSpecial(string, trie.root, index + 1, count + 1, trie)
		if remainingSpecial:
			return True
		
	return checkSpecial(string, node[letter], index + 1, count, trie)

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
		
	def buildTrie(self, string):
		current = self.root
		for letter in string:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current[self.endSymbol] = True