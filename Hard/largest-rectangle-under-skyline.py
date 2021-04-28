
# LARGEST RECTANGLE UNDER SKYLINE

# O(N^2) time and O(1) space
def largestRectangleUnderSkyline(buildings):
    # Write your code here.
	if len(buildings) == 0:
		return 0
	
    maxArea = 0
	for index in range(len(buildings)):
		height = buildings[index]
		area = 0
		for j in reversed(range(index + 1)):
			height = min(height, buildings[j])
			currentArea = height * (index - j + 1)
			area = max(area, currentArea)
		maxArea = max(maxArea, area)
			
	return maxArea
			
# O(N) time and space
def largestRectangleUnderSkyline(buildings):
    # Write your code here.
    pillarIndices = []
	maxArea = 0
	
	for idx, height in enumerate(buildings + [0]):
		while len(pillarIndices) != 0 and buildings[pillarIndices[len(pillarIndices) - 1]] >= height:
			pillarHeight = buildings[pillarIndices.pop()]
			width = idx if len(pillarIndices) == 0 else idx - pillarIndices[len(pillarIndices) - 1] - 1
			maxArea = max(width * pillarHeight, maxArea)
			
		pillarIndices.append(idx)
		
	return maxArea
