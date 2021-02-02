
# MERGE LINKED LIST

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N + M) time, O(1) space
def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    startingNode = headOne if headOne.value < headTwo.value else headTwo
	if startingNode == headOne:
		headOne = headOne.next
	else:
		headTwo = headTwo.next
	finalNode = startingNode
	
	while headOne is not None and headTwo is not None:
		if headOne.value < headTwo.value:
			finalNode.next = headOne
			finalNode = finalNode.next
			headOne = headOne.next
		else:
			finalNode.next = headTwo
			finalNode = finalNode.next
			headTwo = headTwo.next
	
	if headOne is not None:
		finalNode.next = headOne
	if headTwo is not None:
		finalNode.next = headTwo
		
	return startingNode


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N + M) time and space
def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    recursiveMerge(headOne, headTwo, None)
	return headOne if headOne.value < headTwo.value else headTwo

def recursiveMerge(p1, p2, p1Prev):
	if p1 is None:
		p1Prev.next = p2
		return
	if p2 is None:
		return
	
	if p1.value < p2.value:
		recursiveMerge(p1.next, p2, p1)
	else:
		if p1Prev is not None:
			p1Prev.next = p2
		newP2 = p2.next
		p2.next = p1
		recursiveMerge(p1, newP2, p2)
		
