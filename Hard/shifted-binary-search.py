
# SHIFTED BINARY SEARCH

# O(logN) time and space
def shiftedBinarySearch(array, target):
    # Write your code here.
    return binarySearch(array, target, 0, len(array) - 1)

def binarySearch(array, target, left, right):
	if left > right:
		return -1
	
	mid = left + right
	if array[mid] == target:
		return mid
	
	if array[left] <= array[mid]:
		if array[left] <= target < array[mid]:
			return binarySearch(array, target, left, mid - 1)
		else:
			return binarySearch(array, target, mid + 1, right)
		
	else:
		if array[mid] < target <= array[right]:
			return binarySearch(array, target, mid + 1, right)
		else:
			return binarySearch(array, target, left, mid - 1)


# O(logN) time and O(1) space
def shiftedBinarySearch(array, target):
    # Write your code here.
    left = 0
	right = len(array) - 1
	
	while left <= right:
		mid = left + right
		if array[mid] == target:
			return mid

		if array[left] <= array[mid]:
			if array[left] <= target < array[mid]:
				right = mid - 1
			else:
				left = mid + 1

		else:
			if array[mid] < target <= array[right]:
				left = mid + 1
			else:
				right = mid - 1
				
	return -1