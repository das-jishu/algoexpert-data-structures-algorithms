
# RUN LENGTH ENCODING

# O(N) time and space
def runLengthEncoding(string):
    # Write your code here.
    result = []
	currentChar = string[0]
	frequency = 0
	
	for x in string:
		if x == currentChar:
			if frequency < 9:
				frequency += 1
			else:
				result.append(str(frequency) + currentChar)
				frequency = 1
			
		else:
			result.append(str(frequency) + currentChar)
			currentChar = x
			frequency = 1
	
	result.append(str(frequency) + currentChar)
	return "".join(result)