
# MOVE ELEMENT TO END

# O(N) time and O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
	right = len(array) - 1
	
	while left < right:
		while array[left] != toMove and left < right:
			left += 1
			
		while array[right] == toMove and left < right:
			right -= 1
			
		if left >= right:
			break
		array[left], array[right] = array[right], array[left]
		left += 1
		right -= 1
	
	return array