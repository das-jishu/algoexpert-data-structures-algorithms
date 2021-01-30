
# BOGGLE BOARD

#O(WNM8^S) time and O(W + S) space
def boggleBoard(board, words):
    # Write your code here.
    wordsFound = []
	for word in words:
		isWordPresent = False
		for i in range(len(board)):
			if isWordPresent:
				break
			for j in range(len(board[0])):
				if board[i][j] == word[0]:
					isWordPresent = findWord(board, word, i, j, 0)
					if isWordPresent:
						wordsFound.append(word)
						break
	return wordsFound

def findWord(board, word, i, j, index):
	if index >= len(word):
		return True
	
	if i not in range(len(board)) or j not in range(len(board[0])) or board[i][j] is None:
		return False
	
	if board[i][j] != word[index]:
		return False
	
	characterAtPosition = board[i][j]
	board[i][j] = None
	isWordFound = findWord(board, word, i+1, j, index+1) or findWord(board, word, i-1, j, index+1) or findWord(board, word, i, j+1, index+1) or findWord(board, word, i, j-1, index+1) or findWord(board, word, i+1, j+1, index+1) or findWord(board, word, i+1, j-1, index+1) or findWord(board, word, i-1, j+1, index+1) or findWord(board, word, i-1, j-1, index+1)
	board[i][j] = characterAtPosition
	return isWordFound

# O(NM8^S + WS) time and O(NM + WS) space
def boggleBoard(board, words):
    # Write your code here.
    trie = Trie()
	for word in words:
		trie.add(word)
	finalWords = {}
	visited = [[False for letter in row] for row in board]
	for i in range(len(board)):
		for j in range(len(board[i])):
			explore(i, j, board, trie.root, visited, finalWords)
	return list(finalWords.keys())

def explore(i, j, board, trieNode, visited, finalWords):
	if visited[i][j]:
		return
	letter = board[i][j]
	if letter not in trieNode:
		return
	visited[i][j] = True
	trieNode = trieNode[letter]
	if "*" in trieNode:
		finalWords[trieNode["*"]] = True
	neighbors = getNeighbors(i, j, board)
	for neighbor in neighbors:
		explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
	visited[i][j] = False

def getNeighbors(i, j, board):
	neighbors = []
	if i > 0 and j > 0:
		neighbors.append([i-1, j-1])
	if i > 0 and j < len(board[0]) - 1:
		neighbors.append([i-1, j+1])
	if i < len(board) - 1 and j < len(board[0]) - 1:
		neighbors.append([i+1, j+1])
	if i < len(board) - 1 and j > 0:
		neighbors.append([i+1, j-1])
	if i > 0:
		neighbors.append([i-1, j])
	if i < len(board) - 1:
		neighbors.append([i+1, j])
	if j > 0:
		neighbors.append([i, j-1])
	if j < len(board[0]) - 1:
		neighbors.append([i, j+1])
	return neighbors

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
		
	def add(self, word):
		current = self.root
		for letter in word:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current[self.endSymbol] = word