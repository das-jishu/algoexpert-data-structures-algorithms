
# MERGE OVERLAPPING INTERVALS

# O(NlogN) time and O(N) space
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x: x[0])
	final = [intervals[0]]
	
	for index in range(1, len(intervals)):
		interval = intervals[index]
		if interval[0] > final[-1][1]:
			final.append(interval)
		else:
			final[-1][1] = max(interval[1], final[-1][1])
	
	return final