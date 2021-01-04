
# BINARY SEARCH

#ITERATIVE WAY
def binarySearch(array, target):
    # Write your code here.
    left = 0
	right = len(array) - 1
	
	while left <= right:
		mid = (left + right) // 2
		
		if array[mid] == target:
			return mid
		
		if target < array[mid]:
			right = mid - 1
		else:
			left = mid + 1
			
	return -1

#RECURSIVE WAY
def binarySearch(array, target):
    # Write your code here.
	return findNumber(array, target, 0, len(array)-1)

def findNumber(array, target, left, right):
	if left > right:
		return -1
	
	mid = (left + right) // 2
	
	if array[mid] == target:
		return mid
	
	if target < array[mid]:
		return findNumber(array, target, left, mid-1)
	else:
		return findNumber(array, target, mid+1, right)
