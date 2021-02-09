
# QUICK SORT

# BEST: O(nlogn) time, O(logn) space
# AVERAGE: O(nlogn) time, O(logn) space
# WORST: O(n^2) time, O(logn) space
def quickSort(array):
    # Write your code here.
	partition(array, 0, len(array) - 1)
	return array
    
def partition(array, low, high):
	if low < high:
		print("Inside partition")
		pivot = quickSortHelper(array, low, high)
		print("low",low,"high",high,"pivot",pivot)
		partition(array, low, pivot - 1)
		partition(array, pivot + 1, high)
		
def quickSortHelper(array, low, high):
	print("Quicksorthelper")
	pivot = array[low]
	left = low + 1
	right = high
	while right >= left:
		if array[left] > pivot and array[right] < pivot:
			swap(array, left, right)
			left += 1
			right -= 1
		elif array[left] <= pivot:
			left += 1
		elif array[right] >= pivot:
			right -= 1
	swap(array, low, right)
	return right

def swap(array, one, two):
	array[one], array[two] = array[two], array[one]

# BEST: O(nlogn) time, O(logn) space
# AVERAGE: O(nlogn) time, O(logn) space
# WORST: O(n^2) time, O(logn) space
def quickSort(array):
    # Write your code here.
	quickSortHelper(array, 0, len(array) - 1)
	return array
		
def quickSortHelper(array, low, high):
	print("Quicksorthelper")
	if low >= high:
		return
	pivot = array[low]
	left = low + 1
	right = high
	while right >= left:
		if array[left] > pivot and array[right] < pivot:
			swap(array, left, right)
		if array[left] <= pivot:
			left += 1
		if array[right] >= pivot:
			right -= 1
	swap(array, low, right)
	leftSubArrayIsSmaller = right - 1 - low < high - (right + 1)
	if leftSubArrayIsSmaller:
		quickSortHelper(array, low, right - 1)
		quickSortHelper(array, right + 1, high)
	else:
		quickSortHelper(array, right + 1, high)
		quickSortHelper(array, low, right - 1)

def swap(array, one, two):
	array[one], array[two] = array[two], array[one]

