
# SHORTEN PATH

# O(N) time and space
def shortenPath(path):
    # Write your code here.
	startsWithSlash = path[0] == "/"
	tokens = filter(isImportantToken, path.split("/"))
	stack = []
	if startsWithSlash:
		stack.append("")
	for token in tokens:
		if token == "..":
			if len(stack) == 0 or stack[-1] == "..":
				stack.append(token)
			elif stack[-1] != "":
				stack.pop()
		
		else:
			stack.append(token)
			
	if len(stack) == 1 and stack[0] == "":
		return "/"
	return "/".join(stack)

def isImportantToken(token):
	return len(token) > 0 and token != "."
    
