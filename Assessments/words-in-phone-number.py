
# WORDS IN PHONE NUMBER

# O(N^2 + MS) time and O(N^2 + S + M) space, N -> length of phone number
# M -> number of words, S -> length of longest word
def wordsInPhoneNumber(phoneNumber, words):
    # Write your code here.
    mapDigitToLetters = {
		"0": ["0"],
		"1": ["1"],
		"2": ["a", "b", "c"],
		"3": ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"]
	}
	
	finalWords = []
	trie = Trie(phoneNumber)
	
	for word in words:
		if findWord(trie.root, 0, word, mapDigitToLetters):
			finalWords.append(word)
	
	return finalWords

def findWord(currentNode, currentPosition, word, mapDigitToLetters):
	if currentPosition == len(word):
		return True
	
	letter = word[currentPosition]
	for node in currentNode:
		if node == "*":
			continue
		if letter in mapDigitToLetters[node]:
			return findWord(currentNode[node], currentPosition + 1, word, mapDigitToLetters)
		
	return False

class Trie:
	def __init__(self, string):
		self.root = {}
		self.endSymbol = "*"
		self.buildTrie(string)
		
	def buildTrie(self, string):
		for i in range(len(string)):
			current = self.root
			for j in range(i, len(string)):
				if string[j] not in current:
					current[string[j]] = {}
				current = current[string[j]]
			current[self.endSymbol] = True
	
