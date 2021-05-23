
# MINIMUM CHARACTERS FOR WORDS

# O(N * L) time, N - no of words, L - length of longest word
# O(C) space - lower bound, C - no of unique characters
# o(N * L) space - upper bound, since there might be words having all same characters
def minimumCharactersForWords(words):
    # Write your code here.
    characters = {}
	for word in words:
		temp = {}
		for letter in word:
			if letter not in temp:
				temp[letter] = 0
			temp[letter] += 1
			if letter not in characters or characters[letter] < temp[letter]:
				characters[letter] = temp[letter]
	
	result = []
	for char in characters:
		for times in range(characters[char]):
			result.append(char)
			
	return result