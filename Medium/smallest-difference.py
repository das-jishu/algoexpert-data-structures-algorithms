
# SMALLEST DIFFERENCE

# O(NlogN + MlogM) time and O(1) space
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    result = [float("-inf"), float("inf")]
	arrayOne.sort()
	arrayTwo.sort()
	firstPointer = 0
	secondPointer = 0
	
	while firstPointer < len(arrayOne) and secondPointer < len(arrayTwo):
		num1 = arrayOne[firstPointer]
		num2 = arrayTwo[secondPointer]
		absDifferenceOfResult = abs(result[0] - result[1])
		absDifferenceOfCurrent = abs(num1 - num2)
		
		if absDifferenceOfCurrent < absDifferenceOfResult:
			result[0] = num1
			result[1] = num2	
		if num1 < num2:
			firstPointer += 1
		else:
			secondPointer += 1
			
	return result