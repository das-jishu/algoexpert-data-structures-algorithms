
# PERMUTATIONS

# O(N^2.N!) time and O(N.N!) space
def getPermutations(array):
    # Write your code here.
	if len(array) == 0:
		return []
	
	if len(array) == 1:
		return [[array[0]]]
	
	result = []
	for i, x in enumerate(array):
		allPossible = getPermutations(array[:i] + array[i+1:])
		for item in allPossible:
			item.append(x)
			result.append(item)
			
	return result


# O(N.N!) time and space
def getPermutations(array):
    # Write your code here.
    permutations = []
	permutationsHelper(0, array, permutations)
	return permutations

def permutationsHelper(i, array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range(i, len(array)):
			swap(array, i, j)
			permutationsHelper(i + 1, array, permutations)
			swap(array, i, j)
			
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

