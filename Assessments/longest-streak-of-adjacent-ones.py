
# LONGEST STREAK OF ADJACENT ONES

# O(N) time and O(1) space
def longestStreakOfAdjacentOnes(array):
    # Write your code here.
    index = -1
	maximumOnes = 0
	
	for i in range(len(array)):
		if array[i] == 0:
			left = 0
			j = i - 1
			while j >= 0 and array[j] == 1:
				j -= 1
				left += 1
			
			j = i + 1
			right = 0
			while j < len(array) and array[j] == 1:
				j += 1
				right += 1
				
			total = left + right + 1
			if total > maximumOnes:
				maximumOnes = total
				index = i
				
	return index
				
