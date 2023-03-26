
# LONGEST PEAK

# O(N) time and O(1) space
def longestPeak(array):
    # Write your code here.
    highestPeak = 0
	i = 1
	while i < len(array):
		if array[i] <= array[i-1]:
			i += 1
			continue
			
		currentPeak = 1
		while i < len(array) and array[i] > array[i-1]:
			currentPeak += 1
			i += 1
			
		if i ==len(array) or array[i] == array[i-1]:
			continue
			
		while i < len(array) and array[i] < array[i-1]:
			currentPeak += 1
			i += 1
			
		highestPeak = max(highestPeak, currentPeak)
	return highestPeak

# SECOND WAY
# O(N) time and O(1) space
def longestPeak(array):
    # Write your code here.
    highestPeak = 0
	i = 1
	while i < len(array) - 1:
		if not array[i-1] < array[i] > array[i+1]:
			i += 1
			continue
			
		currentPeak = 3
		k = i - 2
		while k >= 0 and array[k] < array[k+1]:
			k -= 1
			currentPeak += 1
			
		k = i + 2
		while k < len(array) and array[k] < array[k-1]:
			k += 1
			currentPeak += 1
			
		i = k
		highestPeak = max(highestPeak, currentPeak)
	return highestPeak
