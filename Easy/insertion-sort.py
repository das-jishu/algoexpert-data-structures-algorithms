
# INSERTION SORT

def insertionSort(array):
    # Write your code here.
    i = 1
	while i < len(array):
		target = array[i]
		k = i - 1
		while k >= 0 and target < array[k]:
			array[k], array[k+1] = array[k+1], array[k]
			k -= 1
		i += 1
	return array