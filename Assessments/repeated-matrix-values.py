
# REPEATED MATRIX VALUES

# O(M * N) time and O(N) space, where M -> number of rows and
# N -> number of columns in input matrix
def repeatedMatrixValues(matrix):
    # Write your code here.
    count, counted = {}, {}
	for num in matrix[0]:
		count[num] = 0
		counted[num] = False
		
	m, n = len(matrix), len(matrix[0])
	for i in range(m):
		# setting counted of every element as False so that it is
		# counted for the first time
		for num in counted:
			counted[num] = False
			
		for j in range(n):
			num = matrix[i][j]
			if num in count and counted[num] == False:
				count[num] += 1
				# setting counted to True so that it is not counted
				# more than once in a row or column
				counted[num] = True
				
	for j in range(n):
		# setting counted of every element as False so that it is
		# counted for the first time
		for num in counted:
			counted[num] = False
			
		for i in range(m):
			num = matrix[i][j]
			if num in count and counted[num] == False:
				count[num] += 1
				# setting counted to True so that it is not counted
				# more than once in a row or column
				counted[num] = True
	
	finalNums = []
	for num in count:
		if count[num] == m + n:
			finalNums.append(num)
			
	return finalNums