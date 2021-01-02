
# O(N) time and space
def twoNumberSum(array, targetSum):
    # Write your code here.
	if len(array) < 2:
		return []
	store = set()
	
	for x in array:
		if targetSum - x in store:
			return [x, targetSum - x]
		else:
			store.add(x)
			
	return []

# O(N^2) time, O(1) space
# run two for loops and compare every pair to see if it matches.

# O(N logN) time and O(1) space
# sort the array first and then use the two pointer approach to find the target sum.

