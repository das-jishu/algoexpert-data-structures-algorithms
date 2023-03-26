
# LOWEST COMMON MANAGER

# O(N) time and O(d) space, n -> total people
def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    return findLowestCommonManager(topManager, reportOne, reportTwo).lowestCommonManager

def findLowestCommonManager(manager, reportOne, reportTwo):
	reportsFound = 0
	for report in manager.directReports:
		info = findLowestCommonManager(report, reportOne, reportTwo)
		if info.lowestCommonManager is not None:
			return info
		reportsFound += info.reportsFound
		
	if manager == reportOne or manager == reportTwo:
		reportsFound += 1
		
	lowestCommonManager = manager if reportsFound == 2 else None
	return Info(lowestCommonManager, reportsFound)

class Info:
	def __init__(self, lcm, reports):
		self.lowestCommonManager = lcm
		self.reportsFound = reports

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
