
# REVERSE WORDS IN STRING

# O(N) time and space
def reverseWordsInString(string):
    # Write your code here.
    string += " "
	newString = ""
	word = ""
	for char in string:
		if char != " ":
			word += char
		else:
			newString = word + " " + newString
			word = ""
			
	return newString[:len(newString) - 1]

# O(N) time and space
def reverseWordsInString(string):
    # Write your code here.
    characters = [char for char in string]
	reverseListRange(characters, 0, len(characters) - 1)
	
	startOfWord = 0
	while startOfWord < len(characters):
		endOfWord = startOfWord
		while endOfWord < len(characters) and characters[endOfWord] != " ":
			endOfWord += 1
			
		reverseListRange(characters, startOfWord, endOfWord - 1)
		startOfWord = endOfWord + 1
		
	return "".join(characters)

def reverseListRange(list, start, end):
	while start < end:
		list[start], list[end] = list[end], list[start]
		start += 1
		end -= 1