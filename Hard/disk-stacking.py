
# DISK STACKING

# O(N^2) time and O(N) space
def diskStacking(disks):
    # Write your code here.
    disks.sort(key=lambda x: x[2])
	maxHeights = [[0, 0]] * len(disks)
	maxHeights[0] = [disks[0][2], None]
	maxStackHeight = 0
	for i in range(1, len(disks)):
		currentDisk = disks[i]
		highest = findHighestStack(maxHeights, disks, i)
		if highest == i:
			maxHeights[i] = [currentDisk[2], None]
		else:
			maxHeights[i] = [currentDisk[2] + maxHeights[highest][0], highest]
		
	return buildSequence(maxHeights, disks)

def findHighestStack(maxHeights, disks, index):
	highestIndex = index
	maxHeight = maxHeights[index][0]
	bottomDisk = disks[index]
	for j in reversed(range(index)):
		topDisk = disks[j]
		if not isValidDisk(topDisk, bottomDisk):
			continue
		if bottomDisk[2] + maxHeights[j][0] > maxHeight:
			maxHeight = bottomDisk[2] + maxHeights[j][0]
			highestIndex = j
	return highestIndex
		
		
def isValidDisk(topDisk, bottomDisk):
	return True if topDisk[0] < bottomDisk[0] and topDisk[1] < bottomDisk[1] and topDisk[2] < bottomDisk[2] else False
		
def buildSequence(maxHeights, disks):
	start = maxHeights.index(max(maxHeights, key=lambda x: x[0]))
	sequence = [disks[start]]
	start = maxHeights[start][1]
	while start != None:
		sequence.append(disks[start])
		start = maxHeights[start][1]
		
	return list(reversed(sequence))
		

# O(N^2) time and O(N) space
# SAME LOGIC AS ABOVE BUT WITH LESS LINES OF CODE
def diskStacking(disks):
    # Write your code here.
    disks.sort(key=lambda disk: disk[2])
	heights = [disk[2] for disk in disks]
	sequences = [None for disk in disks]
	maxHeightIdx = 0
	for i in range(1, len(disks)):
		currentDisk = disks[i]
		for j in range(i):
			otherDisk = disks[j]
			if areValidDimensions(otherDisk, currentDisk):
				if heights[i] <= currentDisk[2] + heights[j]:
					heights[i] = currentDisk[2] + heights[j]
					sequences[i] = j
		if heights[i] >= heights[maxHeightIdx]:
			maxHeightIdx = i
	return buildSequence(disks, sequences, maxHeightIdx)

def areValidDimensions(o, c):
	return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

def buildSequence(array, sequences, currentIdx):
	sequence = []
	while currentIdx is not None:
		sequence.append(array[currentIdx])
		currentIdx = sequences[currentIdx]
	return list(reversed(sequence))

