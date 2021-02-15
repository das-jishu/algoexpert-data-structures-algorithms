
# STAIRCASE TRAVERSAL

# O(NK) time and O(N) space
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return getTotalWays(height, maxSteps, 0, {})

def getTotalWays(height, maxSteps, currentStep, cache):
	if currentStep == height:
		return 1
	
	if currentStep > height:
		return 0
	
	if currentStep in cache:
		return cache[currentStep]
	
	totalWaysFromCurrentStep = 0
	for step in range(1, maxSteps + 1):
		totalWaysFromCurrentStep += getTotalWays(height, maxSteps, currentStep + step, cache)
		
	cache[currentStep] = totalWaysFromCurrentStep
	return cache[currentStep]

#O(N * K) time and O(N) space
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    waysToTop = [0 for _ in range(height + 1)]
	waysToTop[0] = 1
	waysToTop[1] = 1
	
	for currentHeight in range(2, height + 1):
		step = 1
		while step <= maxSteps and step <= currentHeight:
			waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
			step += 1
			
	return waysToTop[height]

# O(N) time and space
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    currentNumberOfWays = 0
	waysToTop = [1]
	
	for currentHeight in range(1, height + 1):
		startOfWindow = currentHeight - maxSteps - 1
		endOfWindow = currentHeight - 1
		if startOfWindow >= 0:
			currentNumberOfWays -= waysToTop[startOfWindow]
			
		currentNumberOfWays += waysToTop[endOfWindow]
		waysToTop.append(currentNumberOfWays)
	
	return waysToTop[height]
