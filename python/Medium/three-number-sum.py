
# THREE NUMBER SUM

# USING HASH TABLES AND EXTRA SPACE
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
	result = []
	
	for i,x in enumerate(array):
		target = targetSum - x
		possibleTwoSums = twoNumberSum(array[i+1:], target)
		for y in possibleTwoSums:
			y.insert(0, x)
			result.append(y)
			
	return result

def twoNumberSum(array, target):
	store = {}
	twoSums = []
	for x in array:
		value = target - x
		if value in store:
			twoSums.insert(0, [value, x])
		store[x] = True
		
	return twoSums

# USING POINTERS. O(N) space and O(N^2) time
def threeNumberSum(array, targetSum):
    # Write your code here.
    result = []
	array.sort()
	
	i = 0
	while i < len(array) - 2:
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				result.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			else:
				right -= 1
		i += 1
	return result
