
# NUMBER OF BINARY TREE TOPOLOGIES

# O(N^2) time and O(N) space
def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    return calculateNumberOfTopologies(n, {0: 1})

def calculateNumberOfTopologies(n, cache):
	if n in cache:
		return cache[n]
	
	total = 0
	for i in range(0, n):
		topologiesInLeftSubtree = calculateNumberOfTopologies(i, cache)
		topologiesInRightSubtree = calculateNumberOfTopologies(n - i - 1, cache)
		total += topologiesInLeftSubtree * topologiesInRightSubtree
	
	cache[n] = total
	return total
		
# O(N^2) time and O(N) space
def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    cache = [1]
	for m in range(1, n + 1):
		numberOfTrees = 0
		for leftTreeSize in range(m):
			rightTreeSize = m - 1 - leftTreeSize
			numberOfLeftTrees = cache[leftTreeSize]
			numberOfRightTrees = cache[rightTreeSize]
			numberOfTrees += numberOfLeftTrees * numberOfRightTrees
		cache.append(numberOfTrees)
	return cache[n]