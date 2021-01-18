
# BALANCED BRACKETS

# O(N) time and space
def balancedBrackets(string):
    # Write your code here.
    matchingBrackets = {")": "(", "}": "{", "]": "["}
	stack = []
	
	for bracket in string:
		if bracket not in [")", "(", "}", "{", "]", "["]:
			continue
		if bracket in ["(", "{", "["]:
			stack.append(bracket)
		else:
			if not stack:
				return False
			if not stack[-1] == matchingBrackets[bracket]:
				return False
			stack.pop()
			
	return len(stack) == 0
