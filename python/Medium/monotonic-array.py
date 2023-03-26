
# MONOTONIC ARRAY

# O(N) time and O(1) space
def isMonotonic(array):
    # Write your code here.
    isMonotonicallyIncreasing = None
	i = 1
	while i < len(array):
		if array[i] == array[i-1]:
			pass
		elif array[i] > array[i-1]:
			if isMonotonicallyIncreasing == False:
				return False
			isMonotonicallyIncreasing = True
		else:
			if isMonotonicallyIncreasing == True:
				return False
			isMonotonicallyIncreasing = False
		i += 1
	return True