
# FIND THREE LARGEST NUMBERS

# SOLUTION 1
def findThreeLargestNumbers(array):
    # Write your code here.
	i = 0
	while i < 3:
		pos = i
		largest = array[pos]
		j = i + 1
		while j < len(array) - 1:
			if array[j] > largest:
				largest = array[j]
				pos = j
			j += 1

		temp = array[i]
		array[i] = array[pos]
		array[pos] = temp
		i += 1
		
	return [array[2], array[1], array[0]]

# SOLUTION 2
def findThreeLargestNumbers(array):
    # Write your code here.
    largestNumbers = [None, None, None]
	for elem in array:
		print(largestNumbers)
		checkAndUpdate(array, elem, largestNumbers)
		
	return largestNumbers

def checkAndUpdate(array, num, largestNumbers):
	if largestNumbers[2] is None or num > largestNumbers[2]:
		updateResult(largestNumbers, num, 2)
	elif not largestNumbers[1] or num > largestNumbers[1]:
		updateResult(largestNumbers, num, 1)
	elif not largestNumbers[0] or num > largestNumbers[0]:
		updateResult(largestNumbers, num, 0)
	else:
		pass
	
def updateResult(largestNumbers, num, index):
	print("Uppdate result")
	for i in range(index+1):
		if i == index:
			largestNumbers[i] = num
		else:
			largestNumbers[i] = largestNumbers[i+1]