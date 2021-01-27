
# WATER AREA

# O(N) time and space
def waterArea(heights):
    # Write your code here.
    leftMaxHeights = [0] * len(heights)
	rightMaxHeights = [0] * len(heights)
	maxLeft = 0
	for i in range(len(heights)):
		leftMaxHeights[i] = maxLeft
		maxLeft = max(maxLeft, heights[i])
		
	maxRight = 0
	for i in reversed(range(len(heights))):
		rightMaxHeights[i] = maxRight
		maxRight = max(maxRight, heights[i])
		
	waterArea = 0
	for i in range(len(heights)):
		if leftMaxHeights[i] <= heights[i] or rightMaxHeights[i] <= heights[i]:
			continue
		waterArea += min(leftMaxHeights[i], rightMaxHeights[i]) - heights[i]
	
	return waterArea

# O(N) time and space
def waterArea(heights):
    # Write your code here.
    leftMaxHeights = [0] * len(heights)
	maxLeft = 0
	for i in range(len(heights)):
		leftMaxHeights[i] = maxLeft
		maxLeft = max(maxLeft, heights[i])
		
	maxRight = 0
	waterArea = 0
	for i in reversed(range(len(heights))):
		if leftMaxHeights[i] <= heights[i] or maxRight <= heights[i]:
			pass
		else:
			waterArea += min(leftMaxHeights[i], maxRight) - heights[i]
		maxRight = max(maxRight, heights[i])
		
	return waterArea

# O(N) time and O(1) space
def waterArea(heights):
    # Write your code here.
	if len(heights) == 0:
		return 0
	
	leftIndex = 0
	rightIndex = len(heights) - 1
	leftMax = heights[leftIndex]
	rightMax = heights[rightIndex]
	surfaceArea = 0
	
	while leftIndex < rightIndex:
		if heights[leftIndex] < heights[rightIndex]:
			leftIndex += 1
			leftMax = max(leftMax, heights[leftIndex])
			surfaceArea += leftMax - heights[leftIndex]
		else:
			rightIndex -= 1
			rightMax = max(rightMax, heights[rightIndex])
			surfaceArea += rightMax - heights[rightIndex]
			
	return surfaceArea
    
"""
Notes
The video explanation of this question covers a solution that runs with linear space, but we can actually also solve this question with constant space (see our written Solution 2).

To do so, we have to realize that, if we just look at the two extremeties of the input array, the smaller of the two values gives us information about water to be trapped in the middle. For example, consider the following simple array:

heights = [4, 0, 6, 0, 10]
Since the leftmost value 4 is smaller than the rightmost value 10, we know that, assuming all values in between are smaller than this leftmost value, we'll trap water equal to the difference between 4 and those values.

Now of course, middle values won't always be smaller than the leftmost value, like the middlemost value in the array above which is 6. In those cases, we update the leftmost value, making the leftmost value effectively contain the greatest most recently visited value to the left.

Broadly speaking, the algorithm works by setting up two pointers—a left and right pointer—at the extremities of the input array and progressively pushing the one that points to the smallest value inward. At each value in between the pointers, we update the relevant left-or-right max value (this depends on which pointer we moved inward), and we add to our final surface area the difference between the relevant left-or-right max value and the current value. We repeat this until the left and right pointers pass each other.

Since we only need to store five values, this algorithm only requires constant space.

Solution 2 implements this algorithm.
"""
