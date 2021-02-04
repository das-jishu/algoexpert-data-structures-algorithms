
# INTERWEAVING STRINGS

# O(2^(N+M)) time and O(N+M) space
def interweavingStrings(one, two, three):
    # Write your code here.
	return check(one, two, three, 0, 0, 0)
	
def check(one, two, three, indexOne, indexTwo, indexThree):
	if indexOne == len(one) and indexTwo == len(two) and indexThree == len(three):
		return True
	if indexThree == len(three):
		return False
	
	matchWithOne = three[indexThree] == one[indexOne] if indexOne < len(one) else False
	matchWithTwo = three[indexThree] == two[indexTwo] if indexTwo < len(two) else False
	if not matchWithOne and not matchWithTwo:
		return False
	if matchWithOne and matchWithTwo:
		return check(one, two, three, indexOne+1, indexTwo, indexThree+1) or check(one, two, three, indexOne, indexTwo+1, indexThree+1)
	if matchWithOne:
		return check(one, two, three, indexOne+1, indexTwo, indexThree+1)
	if matchWithTwo:
		return check(one, two, three, indexOne, indexTwo+1, indexThree+1)

# O(2^(N+M)) time and O(N+M) space
def interweavingStrings(one, two, three):
    # Write your code here.
    if len(three) != len(one) + len(two):
		return False
	
	return areInterwoven(one, two, three, 0, 0)


def areInterwoven(one, two, three, i, j):
	k = i + j
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		if areInterwoven(one, two, three, i+1, j):
			return True
		
	if j < len(two) and two[j] == three[k]:
		return areInterwoven(one, two, three, i, j+1)
	
	return False

# O(NM) time and space
def interweavingStrings(one, two, three):
    # Write your code here.
    if len(three) != len(one) + len(two):
		return False
	
	cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]
	return areInterwoven(one, two, three, 0, 0, cache)


def areInterwoven(one, two, three, i, j, cache):
	if cache[i][j] is not None:
		return cache[i][j]
	
	k = i + j
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		cache[i][j] = areInterwoven(one, two, three, i+1, j, cache)
		if cache[i][j]:
			return True
		
	if j < len(two) and two[j] == three[k]:
		cache[i][j] = areInterwoven(one, two, three, i, j+1, cache)
		return cache[i][j]
	
	cache[i][j] = False
	return False

