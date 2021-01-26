
# MIN NUMBER OF JUMPS

# O(N^2) time and O(N) space
def minNumberOfJumps(array):
    # Write your code here.
    jumps = [0] * len(array)
	
	i = len(jumps) - 2
	while i >= 0:
		stepsAllowed = array[i]
		if i + stepsAllowed >= len(array) - 1:
			jumps[i] = 1
		else:
			minJump = float('inf')
			while stepsAllowed >= 1:
				minJump = min(minJump, 1 + jumps[i + stepsAllowed])
				stepsAllowed -= 1
			jumps[i] = minJump
		i -= 1
	return jumps[0]

# O(N) time and O(1) space
def minNumberOfJumps(array):
    # Write your code here.
    if len(array) == 1:
		return 0
	jumps = 0
	maxReach = array[0]
	steps = array[0]
	for i in range(1, len(array) - 1):
		maxReach = max(maxReach, i + array[i])
		steps -= 1
		if steps == 0:
			jumps += 1
			steps = maxReach - i
	return jumps + 1
