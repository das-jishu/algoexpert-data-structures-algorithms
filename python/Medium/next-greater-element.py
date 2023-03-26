
# NEXT GREATER ELEMENT

# O(N) time and space
def nextGreaterElement(array):
    # Write your code here.
	result = [-1] * len(array)
	stack = [0]
	
	for i in range(2 * len(array)):
		index = i % len(array)
		if len(stack) > 0 and array[index] <= array[stack[-1]]:
			stack.append(index)
			continue
		while stack and array[stack[-1]] < array[index]:
			j = stack.pop()
			result[j] = array[index]
		stack.append(index)
		
	return result
