
# INDEX EQUALS VALUE

# O(N) time and O(1) space
def indexEqualsValue(array):
    # Write your code here.
    for i, elem in enumerate(array):
		if i == elem:
			return i
	return -1


# O(logN) time and O(1) space
def indexEqualsValue(array):
    # Write your code here.
    left = 0
	right = len(array) - 1
	currentMinIndex = -1
	while left <= right:
		mid = (left + right) // 2
		if mid == array[mid]:
			currentMinIndex = mid
			right = mid - 1
		elif array[mid] > mid:
			right = mid - 1
		else:
			left = mid + 1
	
	return currentMinIndex

# O(logN) time and space
def indexEqualsValue(array):
    # Write your code here.
    return searchMinIndex(array, 0, len(array) - 1)

def searchMinIndex(array, left, right):
	if left > right:
		return -1
	
	mid = (left + right) // 2
	if array[mid] > mid:
		return searchMinIndex(array, left, mid - 1)
	elif array[mid] < mid:
		return searchMinIndex(array, mid + 1, right)
	else:
		if mid == 0:
			return 0
		elif array[mid - 1] < mid - 1:
			return mid
		else:
			return searchMinIndex(array, left, mid - 1)
