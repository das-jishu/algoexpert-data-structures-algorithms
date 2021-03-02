
# NUMBER OF WAYS TO TRAVERSE GRAPH

# O(2^(N + M)) time and O(N + M) space
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    return traverseGraph(1, 1, width, height)

def traverseGraph(posx, posy, width, height):
	if posy > height or posx > width:
		return 0
	if posy == height and posx == width:
		return 1
	return traverseGraph(posx + 1, posy, width, height) + traverseGraph(posx, posy + 1, width, height)

# O(N * M) time and space
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    ways = [[1 for _ in range(width)] for _ in range(height)]
	for posy in range(1, height):
		for posx in range(1, width):
			ways[posy][posx] = ways[posy - 1][posx] + ways[posy][posx - 1]
			
	return ways[-1][-1]
			
# O(N + M) time and O(1) space
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    totalWays = factorial(width + height - 2)
	waysHavingSamePattern = factorial(width - 1) * factorial(height - 1)
	totalUniqueWays = totalWays / waysHavingSamePattern
	return totalUniqueWays
	
def factorial(n):
	fact = 1
	while n > 0:
		fact *= n
		n -= 1
	return fact
