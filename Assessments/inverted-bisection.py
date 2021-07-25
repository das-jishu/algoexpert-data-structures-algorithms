
# INVERTED BISECTION

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time and O(1) space
def invertedBisection(head):
    # Write your code here.
	if head is None or head.next is None:
		return head
	
	prev = None
    slow = head
	fast = head
	while fast and fast.next:
		prev = slow
		slow = slow.next
		fast = fast.next.next
		
	hasEvenCount = True if fast == None else False
	prev.next = None
	if hasEvenCount:
		firstHalf = reverseLinkedList(head)
		secondHalf = reverseLinkedList(slow)
		head.next = secondHalf
		return firstHalf
	else:
		firstHalf = reverseLinkedList(head)
		secondHalf = reverseLinkedList(slow.next)
		head.next = slow
		slow.next = secondHalf
		return firstHalf

def reverseLinkedList(head):
	prev = None
	cur = head
	while cur is not None:
		temp = cur.next
		cur.next = prev
		prev = cur
		cur = temp
		
	return prev
		