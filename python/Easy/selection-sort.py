
# SELECTION SORT

def selectionSort(array):
    # Write your code here.
    i = 0
	while i < len(array) - 1:
		j = i + 1
		pos = i
		while j < len(array):
			if array[j] < array[pos]:
				pos = j
			j += 1
		array[i], array[pos] = array[pos], array[i]
		i += 1
		
	return array