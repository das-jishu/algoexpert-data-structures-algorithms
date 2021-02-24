
# AIRPORT CONNECTIONS

# O(A * (A + R) + A + R + Alog(A)) time, O(A + R) space
def airportConnections(airports, routes, startingAirport):
    # Write your code here.
    airportGraph = createAirportGraph(airports, routes)
	unreachableAirportNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
	markUnreachableConnections(airportGraph, unreachableAirportNodes)
	return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)

def createAirportGraph(airports, routes):
	airportGraph = {}
	for airport in airports:
		airportGraph[airport] = AirportNode(airport)
	for route in routes:
		airport, connection = route
		airportGraph[airport].connections.append(connection)
	return airportGraph

def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
	visitedAirports = {}
	depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)
	
	unreachableAirportNodes = []
	for airport in airports:
		if airport in airports:
			if airport in visitedAirports:
				continue
			airportNode = airportGraph[airport]
			airportNode.isReachable = False
			unreachableAirportNodes.append(airportNode)
	return unreachableAirportNodes

def depthFirstTraverseAirports(airportGraph, airport, visitedAirports):
	if airport in visitedAirports:
		return
	visitedAirports[airport] = True
	connections = airportGraph[airport].connections
	for connection in connections:
		depthFirstTraverseAirports(airportGraph, connection, visitedAirports)
		
def markUnreachableConnections(airportGraph, unreachableAirportNodes):
	for airportNode in unreachableAirportNodes:
		airport = airportNode.airport
		unreachableConnections = []
		depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, {})
		airportNode.unreachableConnections = unreachableConnections

def depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
	if airportGraph[airport].isReachable:
		return
	if airport in visitedAirports:
		return
	visitedAirports[airport] = True
	unreachableConnections.append(airport)
	connections = airportGraph[airport].connections
	for connection in connections:
		depthFirstAddUnreachableConnections(airportGraph, connection, unreachableConnections, visitedAirports)
		
def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
	unreachableAirportNodes.sort(key=lambda airport: len(airport.unreachableConnections), reverse=True)
	
	numberOfNewConnections = 0
	for airportNode in unreachableAirportNodes:
		if airportNode.isReachable:
			continue
		numberOfNewConnections += 1
		for connection in airportNode.unreachableConnections:
			airportGraph[connection].isReachable = True
	return numberOfNewConnections

class AirportNode:
	def __init__(self, airport):
		self.airport = airport
		self.connections = []
		self.isReachable = True
		self.unreachableConnections = []
		
