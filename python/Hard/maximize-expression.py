
# MAXIMIZE EXPRESSION

# O(N) time and space
def maximizeExpression(array):
    # Write your code here.
    if len(array) < 4:
		return 0
	
	maxA = [None for _ in array]
	maxA[0] = array[0]
	for index in range(1, len(array)):
		maxA[index] = max(array[index], maxA[index - 1])
	
	maxAminusB = [None for _ in array]
	maxAminusB[1] = maxA[0] - array[1]
	for index in range(2, len(array)):
		currentValue = maxA[index - 1] - array[index]
		maxAminusB[index] = max(maxAminusB[index - 1], currentValue)
		
	maxAminusBplusC = [None for _ in array]
	maxAminusBplusC[2] = maxAminusB[1] + array[2]
	for index in range(3, len(array)):
		currentValue = maxAminusB[index - 1] + array[index]
		maxAminusBplusC[index] = max(maxAminusBplusC[index - 1], currentValue)
		
	maxTotal = [None for _ in array]
	maxTotal[3] = maxAminusBplusC[2] - array[3]
	for index in range(4, len(array)):
		currentValue = maxAminusBplusC[index - 1] - array[index]
		maxTotal[index] = max(maxTotal[index - 1], currentValue)
	
	return maxTotal[-1]