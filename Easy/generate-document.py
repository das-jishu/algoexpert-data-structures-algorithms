
# GENERATE DOCUMENT

# O(M + N) time and O(C) space, C -> no.of unique
# characters in characters string, N -> total
# charatcers in document string, M -> total
# characters in characters string
def generateDocument(characters, document):
    # Write your code here.
    count = {}
	for character in characters:
		if character in count:
			count[character] += 1
		else:
			count[character] = 1
			
	for character in document:
		if character not in count or count[character] < 1:
			return False
		else:
			count[character] -= 1
		
	return True
