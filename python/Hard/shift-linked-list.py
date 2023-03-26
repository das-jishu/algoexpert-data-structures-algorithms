
# SHIFT LINKED LIST

# O(N) time and O(1) space
def shiftLinkedList(head, k):
    # Write your code here.
    count = 0
	cur = head
	while cur is not None:
		cur = cur.next
		count += 1
	
	k = k % count
	if k == 0:
		return head
	
	if k < 0:
		k = count - k
	
	left, right = head, head
	while k > 0:
		right = right.next
		k -= 1
	
	while right.next is not None:
		left = left.next
		right = right.next
		
	newHead = left.next
	left.next = None
	right.next = head
	return newHead

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
