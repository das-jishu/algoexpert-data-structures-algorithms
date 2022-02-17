
# SUM OF LINKED LISTS

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


def batchInsertValues(head: LinkedList, data: list):
    curr = head
    for d in data:
        if head is None:
            head = LinkedList(d)
            curr = head
        else:
            curr.next = LinkedList(d)
            curr = curr.next
        
        
    return head

def printList(head: LinkedList):
    curr = head
    while curr is not None:
        print(str(curr.value), end=" ")
        curr = curr.next
    print("\n")

def extractArithmeticResultFromList(listA: list, listB: list):
    strA = "".join([str(e) for e in listA])
    strB = "".join([str(e) for e in listB])
    return int(strA) + int(strB)
   
def extractArithmeticResultFromLinkedList(head: LinkedList):
    curr = head
    if head is None:
        return -1
    strRes = ''
    while curr is not None:
        strRes += str(curr.value)
        curr = curr.next

    return strRes               

"""
    Reversers a given Linked List by mutation.
    This has to be O(n), where n == len(Linked List).

"""      
def reverseLinkedList(head: LinkedList):
    curr = head
    prev = head
    next = curr.next

    #nothing to be done
    if head is None: 
        return head 
    while curr is not None:
        if curr == head:
            next = curr.next
            curr.next = None
        else:
            next = curr.next
            curr.next = prev
            

        #move into the next element, remember previous.
        prev = curr   
        curr = next
    return prev

"""
    This approach should produce the proper result.
    Time Complexity: O(n+m)
"""
def sumTwoLists(headA: LinkedList, headB: LinkedList):

    """
        Reversing the lists:
        - O(n) + O(m): where n --> len(ListA), m --> len(ListB) 
    """
    headA = reverseLinkedList(headA) 
    headB = reverseLinkedList(headB)

    currA = headA
    currB = headB
    headResult = None
    currRes = headResult

    carry = 0

    """
        This runs on O(n+m) which is linear!
    """
    while (currA is not None) or (currB is not None):
        digitA = currA.value if currA is not None else 0
        digitB = currB.value if currB is not None else 0
        digitSum = digitA + digitB + carry
        carry = 1 if digitSum > 9 else 0

        sumNode = LinkedList(digitSum % 10)
        if headResult is None:
            headResult = sumNode
            currRes =  headResult
        else:
            sumNode.next = currRes
            headResult = sumNode
            currRes = headResult

        #move on next elements
        currA = currA.next if currA is not None else None
        currB = currB.next if currA is not None else None
    
    #a propagation carry exists.
    if carry != 0:
        carryNode = LinkedList(carry)
        carryNode.next = headResult
        return carryNode

    
    return headResult






            

if __name__ == '__main__':
    print("\nComparing..\n")
    valuesA = [9, 9, 9, 8, 9]
    valuesB = [1, 1, 1, 1, 1]
    headA = batchInsertValues(None, valuesA)
    headB = batchInsertValues(None, valuesB)
    headRes = sumOfLinkedLists(headA, headB)
    properResult = extractArithmeticResultFromList(valuesA, valuesB)
    listResult = extractArithmeticResultFromLinkedList(headRes)
    print("Proper addition result is: " + str(properResult))
    print("Result taken from list is [old method - Bug]: " + str(listResult))
    print("Result taken from list is [new method]: " + str(extractArithmeticResultFromLinkedList(sumTwoLists(headA, headB))))

    
    


   

