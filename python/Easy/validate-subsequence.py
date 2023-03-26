
"""  
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
"""

def isValidSubsequence(array, sequence):
    # Write your code here.
    # O(N) time and O(1) space
    if not sequence:
		return False
	
	index = 0
	for x in array:
		if x == sequence[index]:
			if index == len(sequence) - 1:
				return True
			index += 1
			
	return False