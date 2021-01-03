
# NTH FIBONACCI

#ITERATIVE WAY
def getNthFib(n):
    # Write your code here.
	F0 = 0
	F1 = 1
    if n == 1:
		return F0
	
	if n == 2:
		return F1
	
	F2 = 0
	while n > 2:
		F2 = F0 + F1
		F0 = F1
		F1 = F2
		n -= 1
		
	return F2

#RECURSIVE WAY
def getNthFib(n):
    # Write your code here.
    return calculateFibonacci(n, {1: 0, 2: 1})

def calculateFibonacci(n, known):
	if n in known:
		return known[n]
	
	known[n] = calculateFibonacci(n-1, known) + calculateFibonacci(n-2, known)
	return known[n]