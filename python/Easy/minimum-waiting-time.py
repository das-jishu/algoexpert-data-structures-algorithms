
# MINIMUM WAITING TIME

# O(NlogN) time and O(1) space
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
	i = 0
	totalTime = 0
	runningSum = 0
	while i < len(queries):
		totalTime += runningSum
		runningSum += queries[i]
		i += 1
	return totalTime

