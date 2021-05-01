
# NODE SWAP

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time and O(1) space
def nodeSwap(head):
    # Write your code here.
	if not head or not head.next:
		return head
	
	newHead = head.next
	prev = None
	current = head
	while current and current.next:
		prev, current = swapPointers(prev, current, current.next)
    
	return newHead
	
def swapPointers(prev, node1, node2):
	temp = node2.next
	node2.next = node1
	if prev:
		prev.next = node2
	node1.next = temp
	return (node1, temp)
