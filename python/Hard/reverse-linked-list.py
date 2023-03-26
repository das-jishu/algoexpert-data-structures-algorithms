
# REVERSE LINKED LIST

# O(N) time and O(1) space
def reverseLinkedList(head):
    # Write your code here.
    previous = None
	current = head
	while current is not None:
		nextNode = current.next
		current.next = previous
		previous = current
		current = nextNode
		
	return previous
