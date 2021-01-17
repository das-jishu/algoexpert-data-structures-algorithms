
# THREE NUMBER SORT

# O(N) time and O(1) space
def threeNumberSort(array, order):
    # Write your code here.
    x, y, z = 0, 0, 0
	for elem in array:
		if elem == order[0]:
			x += 1
		if elem == order[1]:
			y += 1
		if elem == order[2]:
			z += 1
			
	array.clear()
	while x != 0:
		array.append(order[0])
		x -= 1
	while y != 0:
		array.append(order[1])
		y -= 1
	while z != 0:
		array.append(order[2])
		z -= 1
	
	return array

# O(N) time and O(1) space
def threeNumberSort(array, order):
    # Write your code here.
	first = order[0]
	third = order[2]
	
	firstIndex = 0
	for i in range(len(array)):
		if array[i] == first:
			array[firstIndex], array[i] = array[i], array[firstIndex]
			firstIndex += 1
			
	thirdIndex = len(array) - 1
	for i in reversed(range(len(array))):
		if array[i] == third:
			array[thirdIndex], array[i] = array[i], array[thirdIndex]
			thirdIndex -= 1
			
	return array
    
# O(N) time and O(1) space
def threeNumberSort(array, order):
    # Write your code here.
    first = order[0]
	second = order[1]
	
	firstIndex, secondIndex, thirdIndex = 0, 0, len(array) - 1
	
	while secondIndex <= thirdIndex:
		val = array[secondIndex]
		if val == first:
			array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]
			firstIndex += 1
			secondIndex += 1
		elif val == second:
			secondIndex += 1
		else:
			array[secondIndex], array[thirdIndex] = array[thirdIndex], array[secondIndex]
			thirdIndex -= 1
			
	return array	
	
