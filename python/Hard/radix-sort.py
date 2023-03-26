
# RADIX SORT

# O(d * (n + b)) time and O(n + b) space. n -> no.of elements, b -> base, here it is 10, d -> number of digits in the largest number
def radixSort(array):
    # Write your code here.
    if len(array) == 0:
		return array
	
	maxNum = max(array)
	
	digit = 0
	while digit < len(str(maxNum)):
		countingSort(array, digit)
		digit += 1
		
	return array

def countingSort(array, digit):
	sortedArray = [0] * len(array)
	count = [0] * 10
	
	factor = 10 ** digit
	for num in array:
		d = (num // factor) % 10
		count[d] += 1
	
	for idx in range(1, 10):
		count[idx] += count[idx - 1]
		
	for idx in reversed(range(len(array))):
		d = (array[idx] // factor) % 10
		count[d] -= 1
		sIndex = count[d]
		sortedArray[sIndex] = array[idx]
	
	for idx in range(len(array)):
		array[idx] = sortedArray[idx]
