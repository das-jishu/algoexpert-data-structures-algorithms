
# SEARCH FOR RANGE

# O(N) time and space
def searchForRange(array, target):
    # Write your code here.
    positions = [-1, -1]
	binarySearch(array, target, 0, len(array) - 1, positions)
	return positions
	
def binarySearch(array, target, left, right, positions):
	if left > right:
		return
	
	mid = (left + right) // 2
	if array[mid] != target:
		if array[mid] < target:
			binarySearch(array, target, mid + 1, right, positions)
		else:
			binarySearch(array, target, left, mid - 1, positions)

	else:
		if mid == 0 or array[mid-1] != target:
			positions[0] = mid
		if mid == len(array) - 1 or array[mid+1] != target:
			positions[1] = mid
		if -1 not in positions:
			return
		binarySearch(array, target, mid + 1, right, positions)
		binarySearch(array, target, left, mid - 1, positions)
		
# O(logN) time and space
def searchForRange(array, target):
    # Write your code here.
    positions = [-1, -1]
	binarySearch(array, target, 0, len(array) - 1, positions, True)
	binarySearch(array, target, 0, len(array) - 1, positions, False)
	return positions
	
def binarySearch(array, target, left, right, positions, goLeft):
	if left > right:
		return
	
	mid = (left + right) // 2
	if array[mid] != target:
		if array[mid] < target:
			binarySearch(array, target, mid + 1, right, positions, goLeft)
		else:
			binarySearch(array, target, left, mid - 1, positions, goLeft)

	else:
		if goLeft:
			if mid == 0 or array[mid-1] != target:
				positions[0] = mid
			else:
				binarySearch(array, target, left, mid - 1, positions, goLeft)
		else:
			if mid == len(array) - 1 or array[mid+1] != target:
				positions[1] = mid
			else:
				binarySearch(array, target, mid + 1, right, positions, goLeft)
			
# O(logN) time and O(1) space
def searchForRange(array, target):
    # Write your code here.
    positions = [-1, -1]
	binarySearch(array, target, 0, len(array) - 1, positions, True)
	binarySearch(array, target, 0, len(array) - 1, positions, False)
	return positions
	
def binarySearch(array, target, left, right, positions, goLeft):
	while left <= right:
		mid = (left + right) // 2
		if array[mid] != target:
			if array[mid] < target:
				left = mid + 1
			else:
				right = mid - 1

		else:
			if goLeft:
				if mid == 0 or array[mid-1] != target:
					positions[0] = mid
					break
				else:
					right = mid - 1
			else:
				if mid == len(array) - 1 or array[mid+1] != target:
					positions[1] = mid
					break
				else:
					left = mid + 1

		