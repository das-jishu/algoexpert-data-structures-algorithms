
# PALINDROME CHECK

# O(N) time and space
def isPalindrome(string):
    # Write your code here.
	return string == string[::-1]

# O(N) time and O(1) space
def isPalindrome(string):
    # Write your code here.
    i = 0
	j = len(string) - 1
	while i <= j and string[i] == string[j]:
		i += 1
		j -= 1
	
	return i > j

# O(N) time and space
def isPalindrome(string):
    # Write your code here.
    if len(string) < 2:
		return True
	
	if string[0] != string[-1]:
		return False
	
	return isPalindrome(string[1:len(string)-1])
