
# TASK ASSIGNMENT

# O(NlogN) time and O(N) space
def taskAssignment(k, tasks):
    # Write your code here.
	indices = [i for i in range(len(tasks))]
	indices.sort(key=lambda x: tasks[1] - tasks[0])
	result = []
	i = 0
	while k > 0:
		result.append([indices[i], indices[-1 - i]])
		k -= 1
		
	return result

# O(NlogN) time and O(N) space
def taskAssignment(k, tasks):
    # Write your code here.
	pairedTasks = []
	taskIndices = getTaskIndices(tasks)
	tasks.sort()
	for index in range(k):
		task1 = tasks[index]
		task1Indices = taskIndices[task1]
		task1Index = task1Indices.pop()
		
		task2 = tasks[len(tasks) - 1 - index]
		task2Indices = taskIndices[task2]
		task2Index = task2Indices.pop()
		
		pairedTasks.append([task1Index, task2Index])
		
	return pairedTasks

def getTaskIndices(tasks):
	taskIndices = {}
	
	for index, task in enumerate(tasks):
		if task in taskIndices:
			taskIndices[task].append(index)
		else:
			taskIndices[task] = [index]
		
	return taskIndices

