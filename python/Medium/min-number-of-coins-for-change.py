
# MIN NUMBER OF COINS FOR CHANGE

# O(Nd) time and O(N) space
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	return minNumberOfCoinsForChangeHelper(n, denoms, {})
	
def minNumberOfCoinsForChangeHelper(n, denoms, known):
	if n == 0:
		return 0
	
    if n < min(denoms):
		return -1
	
	if n in known:
		return known[n]
	
	minCoins = float('inf')
	for x in denoms:
		minimum = minNumberOfCoinsForChangeHelper(n-x, denoms, known)
		if minimum != -1:
			minCoins = min(minCoins, 1 + minimum)  
	
	if minCoins == float('inf'):
		minCoins = -1
	known[n] = minCoins
	return known[n]

# O(Nd) time and O(N) space
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    numCoins = [float('inf') for i in range(n + 1)]
	numCoins[0] = 0
	
	for denom in denoms:
		for amount in range(1, len(numCoins)):
			if denom <= amount:
				numCoins[amount] = min(numCoins[amount], 1 + numCoins[amount-denom])
	
	return -1 if numCoins[n] == float('inf') else numCoins[n]
