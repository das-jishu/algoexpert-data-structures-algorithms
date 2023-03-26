
# CAESAR CIPHER ENCRYPTOR

# O(N) time and space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    result = []
	for x in string:
		modifiedasc = ord(x) - 97
		newascii = (modifiedasc + key) % 26
		newChar = chr(97 + newascii)
		result.append(newChar)
		
	return "".join(result)

# O(N) time and space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
	key = key % 26
	result = []
	for x in string:
		index = alphabets.index(x) + key % 26
		result.append(alphabets[index])
		
	return "".join(result)

# O(N) time and space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    result = []
	for letter in string:
		oldValue = ord(letter) - 97
		newValue = (oldValue + key) % 26
		newLetter = chr(97 + newValue)
		result.append(newLetter)
	return "".join(result)