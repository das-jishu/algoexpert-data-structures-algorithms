
# TANDEM BICYCLE

#O(NlogN) time and O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort(reverse=True)
	blueShirtSpeeds.sort(reverse=not fastest)
	
	total = 0
	for index in range(len(redShirtSpeeds)):
		total += max(redShirtSpeeds[index], blueShirtSpeeds[index])
	
	return total
