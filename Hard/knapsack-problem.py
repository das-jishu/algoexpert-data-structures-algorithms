
# KNAPSACK PROBLEM

# O(NC) time and space
def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    knapsack = [[0 for _ in range(capacity + 1)] for _ in range(len(items)+1)]
	
	for i in range(1, len(items) + 1):
		for j in range(1, capacity + 1):
			value = items[i-1][0]
			weight = items[i-1][1]
			if weight > j:
				knapsack[i][j] = knapsack[i-1][j]
			else:
				currentCapacity = value + knapsack[i-1][j-weight]
				knapsack[i][j] = max(knapsack[i-1][j], currentCapacity)
	#print(knapsack)
	return buildSequence(knapsack, items)

def buildSequence(knapsack, items):
	sequence = []
	i = len(knapsack) - 1
	j = len(knapsack[0]) - 1
	while i > 0:
		if knapsack[i][j] == knapsack[i-1][j]:
			i -= 1
		else:
			sequence.append(i-1)
			j -= items[i-1][1]
			i -= 1
			if j == 0:
				break
				
	return [knapsack[-1][-1], list(reversed(sequence))]
			
			
		
