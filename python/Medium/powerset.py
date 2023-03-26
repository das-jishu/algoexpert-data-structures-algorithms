
# POWERSET

# O(N*2^N) time and space
def powerset(array):
    # Write your code here.
    powerset = [[]]
	while len(array):
		temp = array.pop()
		for i in range(len(powerset)):
			currentSet = powerset[i]
			powerset.append(currentSet + [temp])
	
	return powerset
