
# MAX SUBSET SUM NO ADJACENT

# O(2^N) time and space
def maxSubsetSumNoAdjacent(array, i=0):
    # Write your code here.
	if i >= len(array):
		return 0
    maxSum1 = array[i] + maxSubsetSumNoAdjacent(array, i+2)
	maxSum2 = maxSubsetSumNoAdjacent(array, i+1)
	return max(maxSum1, maxSum2)

# O(N) time and space
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not array:
		return 0
	
	if len(array) == 1:
		return array[0]
	
	maxSums = [0] * len(array)
	maxSums[0] = array[0]
	maxSums[1] = max(array[0], array[1])
	i = 2
	while i < len(array):
		maxSums[i] = max(maxSums[i-1], array[i] + maxSums[i-2])
		i += 1
	
	return maxSums[len(array) - 1]
	
# O(N) time and O(1) space
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    i = len(array) - 1
	maxSubsetSum = 0
	maxSubsetSum2 = 0
	maxSubsetSumAtI = 0
	while i >= 0:
		maxSubsetSumAtI = max(array[i] + maxSubsetSum2, maxSubsetSum)
		maxSubsetSum2 = maxSubsetSum
		maxSubsetSum = maxSubsetSumAtI
		i -= 1
		
	return maxSubsetSumAtI
