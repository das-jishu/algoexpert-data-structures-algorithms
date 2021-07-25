
# COUNT CONTAINED PERMUTATIONS

# O(M * U + N) time and O(U) space, where M -> length of big string,
# U -> number of unique characters in small string, N -> length
# of small string.
# U is actually a constant since it can't be greater than 26. and 
# M > N, so M will dissolve N
# So, modified complexities:
# O(M) time and O(1) space, M -> length of big string
def countContainedPermutations(bigString, smallString):
    # Write your code here.
    smallCount, bigCount = {}, {}
	for letter in smallString:
		if letter not in smallCount:
			smallCount[letter] = 0
		smallCount[letter] += 1
		
	bigSize, smallSize = len(bigString), len(smallString)
	start, end, totalCount = 0, 0, 0
	
	while end < bigSize:
		letterToAdd = bigString[end]
		if letterToAdd not in bigCount:
			bigCount[letterToAdd] = 0
		bigCount[letterToAdd] += 1
		
		if end - start == smallSize:
			letterToRemove = bigString[start]
			if bigCount[letterToRemove] == 1:
				del bigCount[letterToRemove]
			else:
				bigCount[letterToRemove] -= 1
			
			start += 1
			
		if matchCounts(bigCount, smallCount):
			totalCount += 1
			
		end += 1		
			
	return totalCount

def matchCounts(bigCount, smallCount):
	for letter in smallCount:
		if letter not in bigCount:
			return False
		if smallCount[letter] != bigCount[letter]:
			return False
		
	return True