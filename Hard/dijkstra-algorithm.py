
# DIJKSTRA'S ALGORITHM

# O(V^2 + E) time and O(V) space, E -> Totsl number of edges
def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    distances = [float('inf')] * len(edges)
	distances[start] = 0
	visited = set()
	calculateShortestPath(edges, distances, start, visited)
	for i, distance in enumerate(distances):
		if distance == float('inf'):
			distances[i] = -1
	return distances
	
def calculateShortestPath(edges, distances, currentVertex, visited):
	visited.add(currentVertex)
	
	for pair in edges[currentVertex]:
		destination = pair[0]
		distance = pair[1]
		pathLength = distances[currentVertex] + distance
		distances[destination] = min(distances[destination], pathLength)
	
	nextVertex = findMinDistance(distances, visited)
	if nextVertex != -1:
		calculateShortestPath(edges, distances, nextVertex, visited)

def findMinDistance(distances, visited):
	minDistance = float('inf')
	minDistancePos = -1
	for i, distance in enumerate(distances):
		if i not in visited and distance < minDistance:
			minDistance = distance
			minDistancePos = i
	return minDistancePos

# O(V^2 + E) time and O(V) space, E -> Totsl number of edges
def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    distances = [float('inf')] * len(edges)
	distances[start] = 0
	visited = set()
	
	while len(visited) != len(edges):
		nextVertex, minDistance = findMinDistance(distances, visited)
		if minDistance == float('inf'):
			break
		visited.add(nextVertex)
		for pair in edges[nextVertex]:
			destination = pair[0]
			distance = pair[1]
			pathLength = distances[nextVertex] + distance
			distances[destination] = min(distances[destination], pathLength)
	
	for i, distance in enumerate(distances):
		if distance == float('inf'):
			distances[i] = -1
	return distances
		
def findMinDistance(distances, visited):
	minDistance = float('inf')
	minDistancePos = -1
	for i, distance in enumerate(distances):
		if i not in visited and distance < minDistance:
			minDistance = distance
			minDistancePos = i
	return minDistancePos, minDistance

# O((V + E)* log(V))  time and O(V) space, E -> Totsl number of edges
def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    distances = [float('inf')] * len(edges)
	distances[start] = 0
	
	minDistanceHeap = MinHeap([(idx, float('inf')) for idx in range(len(edges))])
	minDistanceHeap.update(start, 0)
	
	while not minDistanceHeap.isEmpty():
		nextVertex, minDistance = minDistanceHeap.remove()
		if minDistance == float('inf'):
			break
		
		for pair in edges[nextVertex]:
			destination = pair[0]
			distance = pair[1]
			pathLength = distances[nextVertex] + distance
			if pathLength < distances[destination]:
				distances[destination] = pathLength
				minDistanceHeap.update(destination, pathLength)
	
	for i, distance in enumerate(distances):
		if distance == float('inf'):
			distances[i] = -1
	return distances
	
class MinHeap:

	def __init__(self, array):
		# Do not edit the line below.
		self.vertexMap = {idx: idx for idx in range(len(array))}
		self.heap = self.buildHeap(array)

	def isEmpty(self):
		return len(self.heap) == 0

	# O(N) time and O(1) space
	def buildHeap(self, array):
		# Write your code here.
		firstParent = (len(array) - 2) // 2
		for currentIndex in reversed(range(firstParent + 1)):
			self.siftDown(currentIndex, len(array) - 1, array)
			#print(array)
		return array

	# O(log(n)) time and O(1) space
	def siftDown(self, start, endIdx, heap):
		# Write your code here.
		childOneIdx = start * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = start * 2 + 2 if start * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap][1] < heap[start][1]:
				self.swap(start, idxToSwap, heap)
				start = idxToSwap
				childOneIdx = start * 2 + 1
			else:
				return
		
	# O(log(n)) time and O(1) space
	def siftUp(self, start, heap):
		# Write your code here.
		parentIdx = (start - 1) // 2
		while start > 0 and heap[start][1] < heap[parentIdx][1]:
			self.swap(start, parentIdx, heap)
			start = parentIdx
			parentIdx = (start - 1) // 2
			
	def swap(self, i, j, array):
		self.vertexMap[array[i][0]] = j
		self.vertexMap[array[j][0]] = i
		array[i], array[j] = array[j], array[i]

	# O(log(n)) time and O(1) space
	def remove(self):
		# Write your code here.
		self.swap(0, len(self.heap) - 1, self.heap)
		vertex, distance = self.heap.pop()
		self.vertexMap.pop(vertex)
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return vertex, distance

	def update(self, vertex, value):
		self.heap[self.vertexMap[vertex]] = (vertex, value)
		self.siftUp(self.vertexMap[vertex], self.heap)