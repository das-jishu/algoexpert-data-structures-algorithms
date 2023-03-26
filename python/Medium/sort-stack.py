
# SORT STACK

# O(N^2) time and O(N) space
def sortStack(stack):
    # Write your code here.
	if len(stack) == 0:
		return stack
	top = stack.pop()
	sortStack(stack)
	insertInSortedOrder(stack, top)
	return stack

def insertInSortedOrder(stack, val):
	if not stack or stack[-1] < val:
		stack.append(val)
		return
	
	top = stack.pop()
	insertInSortedOrder(stack, val)
	stack.append(top)
	return