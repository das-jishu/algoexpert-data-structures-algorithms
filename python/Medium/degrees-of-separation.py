
# DEGREES OF SEPARATION

# O(V + E) time, O(V) space
def degreesOfSeparation(friendsLists, personOne, personTwo):
    # Write your code here.
    degrees, visited = {}, {}
	findDegrees(friendsLists, personOne, degrees, visited, 0)
	getUnconnectedPeople(friendsLists, degrees)
	countOne = 0
	for person in degrees:
		if degrees[person] > 6:
			countOne += 1
	
	print(degrees)
	degrees, visited = {}, {}
	findDegrees(friendsLists, personTwo, degrees, visited, 0)
	getUnconnectedPeople(friendsLists, degrees)
	countTwo = 0
	for person in degrees:
		if degrees[person] > 6:
			countTwo += 1
	print(degrees)		
	if countOne < countTwo:
		return personOne
	elif countTwo < countOne:
		return personTwo
	else:
		return ""

def findDegrees(friendsLists, person, degrees, visited, level):
	degrees[person] = 0
	queue = [(person, 0)]
	#visited = {person: True}
	while queue:
		current = queue.pop(0)
		#visited[current[0]] = True
		level = current[1]
		for friend in friendsLists[current[0]]:
			if friend in visited:
				continue
			visited[friend] = True
			degrees[friend] = level + 1
			queue.append((friend, level + 1))


def getUnconnectedPeople(friendsLists, degrees):
	for friend in friendsLists:
		if friend not in degrees:
			degrees[friend] = float("inf")