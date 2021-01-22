
# MIN REWARDS

# O(N^2) time and O(N) space
def minRewards(scores):
    rewards = [1] * len(scores)
	
	i = 1
	while i < len(scores):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1] + 1
		else:
			j = i - 1
			while j >= 0 and scores[j] > scores[j+1]:
				rewards[j] = max(rewards[j], rewards[j+1]+1)
				j -= 1
		i += 1
		
	return sum(rewards)
    
# O(N) time and space
def minRewards(scores):
    # Write your code here.
    localMins = getAllLocalMins(scores)
	rewards = [1] * len(scores)
	for localMin in localMins:
		i = localMin + 1
		while i < len(scores) and scores[i] > scores[i - 1]:
			rewards[i] = max(rewards[i-1] + 1, rewards[i])
			i += 1
		
		i = localMin - 1
		while i >= 0 and scores[i] > scores[i+1]:
			rewards[i] = max(rewards[i+1] + 1, rewards[i])
			i -= 1
	return sum(rewards)
	
def getAllLocalMins(array):
	if len(array) == 1:
		return [0]
	localMins = []
	for i in range(len(array)):
		if i == 0 and array[i] < array[i+1]:
			localMins.append(i)
		if i == len(array) - 1 and array[i] < array[i - 1]:
			localMins.append(i)
		if i not in [0, len(array) - 1] and array[i] < array[i+1] and array[i] < array[i-1]:
			localMins.append(i)
	return localMins

# O(N) time and space
def minRewards(scores):
    # Write your code here.
    rewards = [1] * len(scores)
	for i in range(1, len(scores)):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1] + 1
	for i in reversed(range(len(scores) - 1)):
		if scores[i] > scores[i+1]:
			rewards[i] = max(rewards[i], rewards[i+1] + 1)
	return sum(rewards)
