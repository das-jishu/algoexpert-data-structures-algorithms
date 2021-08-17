
# BUBBLE SORT

# SOLUTION 1
def bubbleSort(array):
    # Write your code here.
    for i in range(len(array)):
		alreadySorted = True
		for j in range(len(array) - i - 1):
			if array[j] > array[j+1]:
				alreadySorted = False
				array[j], array[j+1] = array[j+1], array[j]
		if alreadySorted:
			break
			
	return array

# SOLUTION 2
def bubbleSort(array):
    # Write your code here.
    alreadySorted = False
	i = 0
	while not alreadySorted:
		alreadySorted = True
		for j in range(len(array) - i - 1):
			if array[j] > array[j+1]:
				alreadySorted = False
				array[j], array[j+1] = array[j+1], array[j]
		i += 1
		
	return array

#SOLUTION 3 Using Recursion
def bubbleSort(array,n):
	#Write your code here
	#n is the length of the array
    if n==1:
        print(array)
        return
    for i in range(0,n-1):
        if array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
    bubbleSort(array,n-1)

