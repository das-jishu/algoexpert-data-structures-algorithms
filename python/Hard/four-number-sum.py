
# FOUR NUMBER SUM

# O(N^3) time and O(N^2) space
def fourNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
    fourSums = []
	index = 0
	while index < len(array) - 3:
		allPossibleThreeSums = threeNumberSum(array, index + 1, targetSum - array[index])
		for subset in allPossibleThreeSums:
			fourSums.append(subset + [array[index]])
		index += 1
	return fourSums

def threeNumberSum(array, start, targetSum):
	threeSums = []
	while start < len(array) - 2:
		left = start + 1
		right = len(array) - 1
		
		while left < right:
			currentSum = array[left] + array[right] + array[start]
			if currentSum == targetSum:
				threeSums.append([array[start], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			else:
				right -= 1
		start += 1
	return threeSums

# Average: O(N^2) time and space
# WORST: O(N^3) time and O(N^2) space
def fourNumberSum(array, targetSum):
    # Write your code here.
    allPairSums = {}
	quadruplets = []
	for i in range(1, len(array) - 1):
		for j in range(i+1, len(array)):
			currentSum = array[i] + array[j]
			difference = targetSum - currentSum
			if difference in allPairSums:
				for pair in allPairSums[difference]:
					quadruplets.append(pair + [array[i], array[j]])
		
		for k in range(0, i):
			currentSum = array[i] + array[k]
			if currentSum not in allPairSums:
				allPairSums[currentSum] = [[array[k], array[i]]
			else:
					allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets