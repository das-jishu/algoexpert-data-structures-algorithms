
# GENERATE DIV TAGS

# O(2N!/(N! * (N + 1)!)) time and space
def generateDivTags(numberOfTags):
    # Write your code here.
	allCombinations = []
	generateTags(numberOfTags, numberOfTags, "", allCombinations)
	return allCombinations

def generateTags(openCount, closeCount, current, result):
	if openCount == 0:
		result.append(current + "</div>" * closeCount)
		return
	
	if openCount == closeCount:
		generateTags(openCount - 1, closeCount, current + "<div>", result)
		return
	
	generateTags(openCount - 1, closeCount, current + "<div>", result)
	generateTags(openCount, closeCount - 1, current + "</div>", result)

