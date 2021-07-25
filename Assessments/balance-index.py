
# BALANCE INDEX

# O(N) time and O(1) space, where N -> length of input array
def balanceIndex(array):
    # Write your code here.
    rightSum = sum(array)
	leftSum = 0
	
	for i in range(len(array)):
		leftSum = leftSum + array[i - 1] if i != 0 else leftSum
		rightSum -= array[i]
		if leftSum == rightSum:
			return i
		
	return -1
