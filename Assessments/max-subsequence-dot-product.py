
# MAX SUBSEQUENCE DOT PRODUCT

# O(m * n) time, O(m * n) space; m is the length of arrayOne and 
# n is the length of arrayTwo
def maxSubsequenceDotProduct(arrayOne, arrayTwo):
    # Write your code here.
	# This solution takes care of a situation where the max dot product is less than zero.
	# This covers all edges, so this is the correct optimal solution.
	
	m, n = len(arrayOne), len(arrayTwo)
    dp = [[float("-inf") for i in range(m + 1)] for j in range(n + 1)]
	
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			first = arrayOne[j - 1]
			second = arrayTwo[i - 1]
			product = first * second
			sum = product if dp[i - 1][j - 1] == float("-inf") else dp[i - 1][j - 1] + product
			dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], sum)
	
	return dp[-1][-1]
	