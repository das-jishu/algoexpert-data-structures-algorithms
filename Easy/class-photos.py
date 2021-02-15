
# CLASS PHOTOS

# O(NlogN) time and O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
	blueShirtHeights.sort()
	if redShirtHeights[0] == blueShirtHeights[0]:
		return False 
	direction = True if redShirtHeights[0] > blueShirtHeights[0] else False
	i = 1
	while i < len(redShirtHeights):
		height1 = redShirtHeights[i]
		height2 = blueShirtHeights[i]
		if not compareHeights(height1, height2, direction):
			return False
		i += 1
	return True

def compareHeights(height1, height2, direction):
	if direction:
		return True if height1 > height2 else False
	else:
		return True if height1 < height2 else False
