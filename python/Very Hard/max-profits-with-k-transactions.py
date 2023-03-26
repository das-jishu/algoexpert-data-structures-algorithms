
# MAX PROFITS WITH K TRANSACTIONS

# O(nk) time and space
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if not len(prices):
		return 0
	profits = [[0 for d in prices] for t in range(k + 1)]
	for t in range(1, k + 1):
		maxThusFar = float("-inf")
		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
			profits[t][d] = max(profits[t][d - 1], maxThusFar + prices[d])
	return profits[-1][-1]

# O(nk) time and O(n) space
def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if not len(prices):
		return 0
	evenProfits = [0 for d in prices]
	oddProfits = [0 for d in prices]
	for t in range(1, k + 1):
		maxThusFar = float("-inf")
		if t % 2 == 1:
			currentProfits = oddProfits
			previousProfits = evenProfits
		else:
			currentProfits = evenProfits
			previousProfits = oddProfits
		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d - 1])
			currentProfits[d] = max(currentProfits[d - 1], maxThusFar + prices[d])
	return evenProfits[-1] if k % 2 == 0 else oddProfits[-1]