
# CYCLE IN GRAPH

# O(V + E) time and O(V) space
def cycleInGraph(edges):
    # Write your code here.
	alreadyVisited = [False for i in range(len(edges))]
    for i, x in enumerate(edges):
		if alreadyVisited[i]:
			continue
		if not isCyclePresent(i, edges, set(), alreadyVisited):
			continue
		else:
			return True
	return False

def isCyclePresent(current, edges, visited, alreadyVisited):
	alreadyVisited[current] = True
	if current in visited:
		return True
	visited.add(current)
	for neighbor in edges[current]:
		if alreadyVisited[neighbor] and neighbor not in visited:
			continue
		if not isCyclePresent(neighbor, edges, visited, alreadyVisited):
			continue
		else:
			return True
	visited.remove(current)
	return False