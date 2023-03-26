
# NON-CONSTRUCTIBLE CHANGE

# O(NlogN) time, O(1) space
def nonConstructibleChange(coins):
    # Write your code here.
    if not coins:
		return 1
	
	coins.sort()
	maxChangeGenerated = 0
	i = 0
	while i < len(coins):
		print(i,maxChangeGenerated)
		if coins[i] <= maxChangeGenerated + 1:
			maxChangeGenerated += coins[i]
		else:
			return maxChangeGenerated + 1
		i += 1
	
	return maxChangeGenerated + 1
	

