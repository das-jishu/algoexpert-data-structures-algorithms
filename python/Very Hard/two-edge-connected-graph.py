
# TWO EDGE CONNECTED GRAPH

# O(V + E) time and O(V) space
def twoEdgeConnectedGraph(edges):
    # Write your code here.
    if len(edges) == 0:
		return True
	
	arrivalTimes = [-1] * len(edges)
	startVertex = 0
	
	if getMinTime(startVertex, -1, 0, arrivalTimes, edges) == -1:
		return False
	
	return areAllVerticesVisited(arrivalTimes)

def areAllVerticesVisited(arrivalTimes):
	for time in arrivalTimes:
		if time == -1:
			return False
		
	return True

def getMinTime(currentVertex, parent, currentTime, arrivalTimes, edges):
	arrivalTimes[currentVertex] = currentTime
	minimumArrivalTime = currentTime
	
	for destination in edges[currentVertex]:
		if arrivalTimes[destination] == -1:
			minimumArrivalTime = min(minimumArrivalTime, getMinTime(destination, currentVertex, currentTime + 1, arrivalTimes, edges))
		elif destination != parent:
			minimumArrivalTime = min(minimumArrivalTime, arrivalTimes[destination])
		
	if minimumArrivalTime == currentTime and parent != -1:
		return -1
	
	return minimumArrivalTime
