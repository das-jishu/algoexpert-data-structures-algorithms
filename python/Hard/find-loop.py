
# FIND LOOP

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time and O(1) space
def findLoop(head):
    # Write your code here.
    slow = head.next
	fast = head.next.next
	while slow != fast:
		slow = slow.next
		fast = fast.next.next
		
	current = head
	while current != fast:
		current = current.next
		fast = fast.next
	
	return current
