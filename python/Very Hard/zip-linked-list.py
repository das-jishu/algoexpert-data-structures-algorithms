
# ZIP LINKED LIST

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time and O(1) space
def zipLinkedList(linkedList):
    # Write your code here.
	if not linkedList or not linkedList.next:
		return linkedList
	
    slow = linkedList
	fast = linkedList
	
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		
	reverseHead = reverseLinkedList(slow.next)
	slow.next = None
	current = linkedList
	currentReverse = reverseHead
	while currentReverse != None:
		temp = current.next
		tempReverse = currentReverse.next
		current.next = currentReverse
		currentReverse.next = temp
		current = temp
		currentReverse = tempReverse
		
	return linkedList

def reverseLinkedList(head):
	if not head:
		return None
	previous = None
	current = head
	while current != None:
		temp = current.next
		current.next = previous
		previous = current
		current = temp
		
	return previous