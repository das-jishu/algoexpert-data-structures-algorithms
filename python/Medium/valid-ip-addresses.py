
# VALID IP ADDRESSES

# O(1) time and space
def validIPAddresses(string):
    # Write your code here.
    validIPAddresses = []
	if len(string) < 4:
		return []
	for i in range(3):
		if not isValidPart(string[:i+1]):
			continue
		for j in range(i+1, i+4):
			if not isValidPart(string[i+1:j+1]):
				continue
			for k in range(j+1, j+4):
				if not isValidPart(string[j+1:k+1]) or not isValidPart(string[k+1:]):
					continue
				validIP = string[:i+1] + "." + string[i+1:j+1] + "." + string[j+1:k+1] + "." + string[k+1:]
				validIPAddresses.append(validIP)
	return validIPAddresses
	

def isValidPart(string):
	if len(string) == 1:
		return True
	if not 0 < len(string) < 4 or string[0] == "0":
		return False
	return 0 <= int(string) <= 255
		