
# REMOVE DUPLICATES FROM LINKED LIST

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time and O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    if not linkedList or not linkedList.next:
		return linkedList
	
	current = linkedList
	while current.next is not None:
		if current.value == current.next.value:
			current.next = current.next.next
		else:
			current = current.next
			
	return linkedList
