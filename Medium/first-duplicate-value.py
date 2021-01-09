
# FIRST DUPLICATE VALUE

# O(N) time and space
def firstDuplicateValue(array):
    # Write your code here.
    store = set()
	for x in array:
		if x not in store:
			store.add(x)
		else:
			return x
	return -1

# O(N) time and O(1) space
def firstDuplicateValue(array):
    # Write your code here.
	i = 0
	while i < len(array):
		x = abs(array[i])
		if array[x-1] < 0:
			return x
		array[x-1] *= -1
		i += 1
		
	return -1