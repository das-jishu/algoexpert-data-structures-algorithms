
# KADANE'S ALGORITHM

# O(N) time and O(1) space
def kadanesAlgorithm(array):
    # Write your code here.
    maxSum = float('-inf')
	currentSum = float('-inf')
	for x in array:
		currentSum = max(currentSum + x, x)
		maxSum = max(currentSum, maxSum)
	return maxSum
