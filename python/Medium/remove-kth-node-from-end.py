
# REMOVE KTH NODE FROM END

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time and O(1) space
def removeKthNodeFromEnd(head, k):
    # Write your code here.
    prev = None
	start = head
	end = head
	while k > 0:
		end = end.next
		k -= 1
		
	while end:
		prev = start
		start = start.next
		end = end.next
		
	if not prev:
		head.value = head.next.value
		head.next = head.next.next
	else:
		prev.next = start.next

