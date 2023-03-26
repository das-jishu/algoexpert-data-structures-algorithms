
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#O(N) time and O(1) space
def linkedListPalindrome(head):
    # Write your code here.
    firstHalf, secondHalf = divideLinkedList(head)
	secondHalf = reverseLinkedList(secondHalf)
	return checkPalindrome(firstHalf, secondHalf)
	
def divideLinkedList(head):
	firstHalf, secondHalf = head, None
	slow, fast = head, head
	previous = None
	while fast.next is not None and fast.next.next is not None:
		previous = slow
		slow = slow.next
		fast = fast.next.next
		
	secondHalf = slow.next
	if fast.next is None:
		if previous is not None:
			previous.next = None
	else:
		slow.next = None
	return (firstHalf, secondHalf)
	
def reverseLinkedList(head):
	previous, current = None, head
	while current is not None:
		temp = current.next
		current.next = previous
		previous = current
		current = temp
	return previous

def checkPalindrome(firstHalf, secondHalf):
	while firstHalf is not None and secondHalf is not None:
		if firstHalf.value != secondHalf.value:
			return False
		firstHalf = firstHalf.next
		secondHalf = secondHalf.next
	return True
		
	
