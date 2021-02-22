
# LONGEST STRING CHAIN

def longestStringChain(strings):
    # Write your code here.
	strings.sort(key=len)
	stringChains = {}
	for string in strings:
    	stringChains[string] = [string]
	maxChainLengthString = strings[0]
	maxChainLength = 0
	for i in range(1, len(strings)):
		string = strings[i]
		index = 0
		currentChainLength = 0
		while index < len(string):
			newString = string[:index] + string[index+1:]
			if newString not in stringChains:
				index += 1
				continue
			existingChain = stringChains[newString]
			if len(existingChain) + 1 > currentChainLength:
				stringChains[string] = [string] + existingChain
				currentChainLength = len(stringChains[string])
				if currentChainLength > maxChainLength:
					maxChainLength = currentChainLength
					maxChainLengthString = string
			index += 1
			
	return stringChains[maxChainLengthString] if maxChainLength > 1 else []


# O(N * M^2 + NlogN) time and O(NM) space
def longestStringChain(strings):
    # Write your code here.
    stringChains = {}
	for string in strings:
		stringChains[string] = {"nextString": "", "maxChainLength": 1}
		
	sortedStrings = sorted(strings, key=len)
	for string in sortedStrings:
		findLongestStringChain(string, stringChains)
	
	return buildLongestStringChain(strings, stringChains)

def findLongestStringChain(string, stringChains):
	for i in range(len(string)):
		smallerString = getSmallerString(string, i)
		if smallerString not in stringChains:
			continue
		tryUpdateLongestStringChain(string, smallerString, stringChains)
		
def getSmallerString(string, index):
	return string[0:index] + string[index + 1:]

def tryUpdateLongestStringChain(currentString, smallerString, stringChains):
	smallerStringChainLength = stringChains[smallerString]["maxChainLength"]
	currentStringChainLength = stringChains[currentString]["maxChainLength"]
	if smallerStringChainLength + 1 > currentStringChainLength:
		stringChains[currentString]["maxChainLength"] = smallerStringChainLength + 1
		stringChains[currentString]["nextString"] = smallerString
		
def buildLongestStringChain(strings, stringChains):
	maxChainLength = 0
	chainStartingString = ""
	for string in strings:
		if stringChains[string]["maxChainLength"] > maxChainLength:
			maxChainLength = stringChains[string]["maxChainLength"]
			chainStartingString = string
			
	ourLongestStringChain = []
	currentString = chainStartingString
	while currentString != "":
		ourLongestStringChain.append(currentString)
		currentString = stringChains[currentString]["nextString"]
		
	return [] if len(ourLongestStringChain) == 1 else ourLongestStringChain