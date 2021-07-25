
# BUILD FAILURES

# O(N*log(S)) time, O(1) space, where N -> length of buildRuns array
# S -> length of longest buildRun
def buildFailures(buildRuns):
    # Write your code here.
    longestRun = 0
	currentRun = 1
	currentHighest = float("-inf")
	
	for buildRun in buildRuns:
		start = 0
		end = len(buildRun) - 1
		mid = 0
		while start <= end:
			mid = (start + end) // 2
			if buildRun[mid] == False:
				if buildRun[mid - 1] == True:
					break
				else:
					end = mid - 1
			
			else:
				start = mid + 1		
		
		totalBuilds = len(buildRun)
		percentage = mid / totalBuilds * 100
		
		if percentage >= currentHighest:
			currentRun = 1
		else:
			currentRun += 1
			
		currentHighest = percentage	
		longestRun = max(longestRun, currentRun)
			
	return longestRun if longestRun > 1 else -1