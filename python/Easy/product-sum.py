""" 
# PRODUCT SUM

Write a function that takes in a "special" array and returns its product sum. 
A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth. 
The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1 ; the depth of the inner array in [[]] is 2 ; the depth of the innermost array in [[[]]] is 3 . 
Therefore, the product sum of [x, y] is x + y ; the product sum of [x, [y, z]] is x + 2 * (y + z) ; the product sum of [x, [y, [z]] ] is x + 2 * (y + 3z) .

Sample Input:
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]] 

Sample Output:
12 // calcuiated as: 5 + 2 + 2 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4) 
"""

# RECURSIVE WAY
def productSum(array):
    # Write your code here.
	return specialArrays(array, 1)
    pass

def specialArrays(array, currentLevel):
	if not array:
		return 0
	
	sum = 0
	for elem in array:
		if type(elem) == list:
			sum += specialArrays(elem, currentLevel + 1)
		else:
			sum += elem
			
	return sum * currentLevel