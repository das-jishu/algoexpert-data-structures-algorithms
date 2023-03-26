
# SUM OF LINKED LISTS

# IN THIS SCENARIO, THE HEAD OF THE LINKED LISTS (BOTH INPUT AND OUTPUT) WOULD POINT TO THE LEAST SIGNIFICANT DIGIT.
# SO, 2 -> 6 IS ACTUALLY 62. 
# IF INPUTS ARE 2 -> 4 and 1 -> 5, THE OUTPUT WILL BE 3 -> 9 which is correct as 42 + 51 = 93 

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(N, M)) time and space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    headOfNew = None
	currentOfNew = headOfNew
	currentOne = linkedListOne
	currentTwo = linkedListTwo
	carry = 0
	
	while currentOne != None or currentTwo != None:
		digitOne = currentOne.value if currentOne != None else 0
		digitTwo = currentTwo.value if currentTwo != None else 0
		
		value = digitOne + digitTwo + carry
		carry = 1 if value > 9 else 0
		
		newNode = LinkedList(value % 10)
		if headOfNew is None:
			headOfNew = newNode
			currentOfNew = headOfNew
		else:
			currentOfNew.next = newNode
			currentOfNew = currentOfNew.next
			
		currentOne = currentOne.next if currentOne != None else currentOne
		currentTwo = currentTwo.next if currentTwo != None else currentTwo
	
	if carry > 0:
		currentOfNew.next = LinkedList(carry)
	
	return headOfNew
