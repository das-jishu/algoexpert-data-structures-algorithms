
# BUBBLE SORT

# SOLUTION 1
def bubbleSort(array):
    # Write your code here.
    for i in range(len(array)):
		alreadySorted = True
		for j in range(len(array) - i - 1):
			if array[j] > array[j+1]:
				alreadySorted = False
				array[j], array[j+1] = array[j+1], array[j]
		if alreadySorted:
			break
			
	return array

# SOLUTION 2
def bubbleSort(array):
    # Write your code here.
    alreadySorted = False
	i = 0
	while not alreadySorted:
		alreadySorted = True
		for j in range(len(array) - i - 1):
			if array[j] > array[j+1]:
				alreadySorted = False
				array[j], array[j+1] = array[j+1], array[j]
		i += 1
		
	return array
