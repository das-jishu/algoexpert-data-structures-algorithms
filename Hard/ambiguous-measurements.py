
# AMBIGUOUS MEASUREMENTS

# O(low * high * n) time and O(low * high) space
def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
    cache = {}
	return canMeasureInRange(measuringCups, low, high, cache)

def canMeasureInRange(measuringCups, low, high, cache):
	key = createKey(low, high)
	if key in cache:
		return cache[key]
	
	if low <= 0 and high <= 0:
		return False
	
	check = False
	for cup in measuringCups:
		cupLow, cupHigh = cup
		if low <= cupLow and cupHigh <= high:
			check = True
			break
			
		newLow = max(0, low - cupLow)
		newHigh = max(0, high - cupHigh)
		check = canMeasureInRange(measuringCups, newLow, newHigh, cache)
		if check:
			break
			
	cache[key] = check
	return check

def createKey(low, high):
	return str(low) + "-" + str(high)