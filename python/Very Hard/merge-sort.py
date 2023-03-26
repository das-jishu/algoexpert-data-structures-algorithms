
# MERGE SORT

# O(NlogN) time and space
def mergeSort(array):
    # Write your code here.
    if len(array) == 1:
		return array
	middle = len(array) // 2
	leftHalf = array[:middle]
	rightHalf = array[middle:]
	leftHalf = mergeSort(leftHalf)
	rightHalf = mergeSort(rightHalf)
	return mergeTwoArrays(leftHalf, rightHalf)

def mergeTwoArrays(array1, array2):
	array = [None] * (len(array1) + len(array2))
	index1 = index2 = index = 0
	while index1 < len(array1) and index2 < len(array2):
		if array1[index1] < array2[index2]:
			array[index] = array1[index1]
			index1 += 1
		else:
			array[index] = array2[index2]
			index2 += 1
		index += 1
	while index1 < len(array1):
		array[index] = array1[index1]
		index += 1
		index1 += 1
	while index2 < len(array2):
		array[index] = array2[index2]
		index += 1
		index2 += 1
	return array

# O(NlogN) time and O(N) space
def mergeSort(array):
    # Write your code here.
    if len(array) <= 1:
		return array
	auxillary = array[:]
	mergeSortHelper(array, 0, len(array) - 1, auxillary)
	return array

def mergeSortHelper(array, start, end, auxillary):
	if start == end:
		return
	middle = (start + end) // 2
	mergeSortHelper(auxillary, start, middle, array)
	mergeSortHelper(auxillary, middle + 1, end, array)
	mergeTwoArrays(array, start, middle, end, auxillary)


def mergeTwoArrays(auxillary, start, middle, end, array):
	index1 = start
	index2 = middle + 1
	index = start
	while index1 <= middle and index2 <= end:
		if array[index1] < array[index2]:
			auxillary[index] = array[index1]
			index1 += 1
		else:
			auxillary[index] = array[index2]
			index2 += 1
		index += 1
	while index1 <= middle:
		auxillary[index] = array[index1]
		index += 1
		index1 += 1
	while index2 <= end:
		auxillary[index] = array[index2]
		index += 1
		index2 += 1