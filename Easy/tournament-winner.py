
# TOURNAMENT WINNER

# O(N+K) time and O(K) space
def tournamentWinner(competitions, results):
    # Write your code here.
    teams = {}
	i = 0
	while i < len(competitions):
		homeTeam = str(competitions[i][0])
		awayTeam = str(competitions[i][1])
		if results[i] == 1:
			if homeTeam in teams:
				teams[homeTeam] += 3
			else:
				teams[homeTeam] = 3
				
		else:
			if awayTeam in teams:
				teams[awayTeam] += 3
			else:
				teams[awayTeam] = 3
		i += 1
	
	return max(teams, key=teams.get)
			
# O(N) time and O(K) space
def tournamentWinner(competitions, results):
    # Write your code here.
    teams = {"": 0}
	i = 0
	currentBestTeam = ""
	while i < len(competitions):
		homeTeam = str(competitions[i][0])
		awayTeam = str(competitions[i][1])
		if results[i] == 1:
			if homeTeam in teams:
				teams[homeTeam] += 3
			else:
				teams[homeTeam] = 3
			currentBestTeam = homeTeam if teams[currentBestTeam] < teams[homeTeam] else currentBestTeam
				
		else:
			if awayTeam in teams:
				teams[awayTeam] += 3
			else:
				teams[awayTeam] = 3
			currentBestTeam = awayTeam if teams[currentBestTeam] < teams[awayTeam] else currentBestTeam
		i += 1
	
	return currentBestTeam
			
