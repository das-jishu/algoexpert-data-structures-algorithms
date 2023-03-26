
# REARRANGE LINKED LIST

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time and O(1) space
def rearrangeLinkedList(head, k):
    # Write your code here.
    headOfSmall = None
	pointerSmall = None
	headOfLarge = None
	pointerLarge = None
	current = head
	nodeWithValueK = None
	pointerNodeWithValueK = None
	
	while current is not None:
		if current.value < k:
			if headOfSmall is None:
				headOfSmall = current
				pointerSmall = current
			else:
				pointerSmall.next = current
				pointerSmall = pointerSmall.next
		elif current.value == k:
			if nodeWithValueK is None:
				nodeWithValueK = current
				pointerNodeWithValueK = current
			else:
				pointerNodeWithValueK.next = current
				pointerNodeWithValueK = pointerNodeWithValueK.next
		else:
			if headOfLarge is None:
				headOfLarge = current
				pointerLarge = current
			else:
				pointerLarge.next = current
				pointerLarge = pointerLarge.next
		current = current.next
	
	if pointerLarge is not None:
		pointerLarge.next = None	
	if nodeWithValueK is None:
		if pointerSmall is None:
			return headOfLarge
		else:
			pointerSmall.next = headOfLarge
			return headOfSmall
	else:
		if pointerSmall is None:
			pointerNodeWithValueK.next = headOfLarge
			return nodeWithValueK
		else:
			pointerSmall.next = nodeWithValueK
			pointerNodeWithValueK.next = headOfLarge
			return headOfSmall
	