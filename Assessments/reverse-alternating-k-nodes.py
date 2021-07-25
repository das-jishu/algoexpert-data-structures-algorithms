
# REVERSE ALTERNATING K NODES

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time and O(1) space, where N is the number of nodes in the 
# linked list
def reverseAlternatingKNodes(head, k):
    # Write your code here.
    t = 0
	
	toggleReverse = True
	startOfReverseSection, current = head, head
	isHeadSet = False
	parent, prevOfReverseSection = None, None
	
	while current is not None:
		if toggleReverse == True:
			if t < k:
				temp = current.next
				current.next = parent
				parent = current
				current = temp
				t += 1
			else:
				head = parent if isHeadSet == False else head
				isHeadSet = True
				startOfReverseSection.next = current
				if prevOfReverseSection is not None:
					prevOfReverseSection.next = parent
				toggleReverse = False
				
		else:
			if t > 0:
				parent = current
				current = current.next
				t -= 1
			else:
				toggleReverse = True
				startOfReverseSection = current
				prevOfReverseSection = parent
	
	# checking if the last section is in reverse mode, then 
	# we need to set all the pointers correctly one last time.
	if toggleReverse == True:
		startOfReverseSection.next = None
		if prevOfReverseSection is not None:
			prevOfReverseSection.next = parent
	
	# isHeadSet can be false here if k is greater than number of nodes
	return head if isHeadSet else parent
				