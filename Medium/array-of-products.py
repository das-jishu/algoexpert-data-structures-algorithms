
# ARRAY OF PRODUCTS

# O(N) time and space
def arrayOfProducts(array):
    # Write your code here.
	# O(N) time, space
    left, right = [0] * len(array), [0] * len(array)
	left[0] = 1
	right[len(array) - 1] = 1
	
	for i in range(1, len(array)):
		left[i] = left[i-1] * array[i-1]
	
	for i in reversed(range(len(array) - 1)):
		right[i] = right[i+1] * array[i+1]
		
	result = []
	for i in range(len(array)):
		result.append(left[i] * right[i])
		
	return result

# O(N) time and space
def arrayOfProducts(array):
    # Write your code here.
	# O(N) time and space
    left = [0] * len(array)
	left[0] = 1
	right = 1
	
	for i in range(1, len(array)):
		left[i] = left[i-1] * array[i-1]
	
	result = []
	for i in reversed(range(len(array))):
		result.insert(0, left[i] * right)
		right *= array[i]
		
	return result

# O(N) time and space
def arrayOfProducts(array):
    # Write your code here.
	result = [1] * len(array)
	
	for i in range(1, len(array)):
		result[i] = result[i-1] * array[i-1]
		
	right = 1
	for i in reversed(range(len(array))):
		result[i] = result[i] * right
		right *= array[i]
		
	return result