
# LINE THROUGH POINTS

# O(N^2) time and O(N) space
def lineThroughPoints(points):
    # Write your code here.
    maxPoints = 1
    for idx, p1 in enumerate(points):
		slopes = {}
		for idx2 in range(idx + 1, len(points)):
			p2 = points[idx2]
			rise, run = getSlope(p1, p2)
			key = createKey(rise, run)
			if key in slopes:
				slopes[key] += 1
			else:
				slopes[key] = 2
			maxPoints = max(maxPoints, slopes[key])
		print(p1, slopes)
	return maxPoints
			
def getSlope(p1, p2):
	if p1[0] == p2[0]:
		return [1, 0]
	else:
		return (p2[1] - p1[1], p2[0] - p1[0])

def createKey(rise, run):
	gcd = getGcd(abs(rise), abs(run))
	rise = rise // gcd
	run = run // gcd
	if rise < 0 and run < 0:
		rise = abs(rise)
		run = abs(run)
	elif run < 0:
		rise = rise * -1
		run = abs(run)
	return str(rise) + ":" + str(run)

def getGcd(a, b):
	if b == 0:
		return a
	return getGcd(b, a % b)