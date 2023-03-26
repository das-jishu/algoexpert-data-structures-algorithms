
# MIN HEIGHT BST

# O(NlogN) time and O(N) space
def minHeightBst(array):
	return minHeightHelper(array, None, 0, len(array) - 1)
		
def minHeightHelper(array, nodeBST, start, end):
	if start > end:
		return
	
	mid = (start + end) // 2
	if not nodeBST:
		nodeBST = BST(array[mid])
	else:
		nodeBST.insert(array[mid])
	minHeightHelper(array, nodeBST, start, mid - 1)
	minHeightHelper(array, nodeBST, mid + 1, end)
	return nodeBST

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

# O(N) time and space
""" def minHeightBst(array):
    return minHeightHelper(array, 0, len(array) - 1)

def minHeightHelper(array, start, end):
	if start > end:
		return None
	
	mid = (start + end) // 2
	newNode = BST(array[mid])
	newNode.left = minHeightHelper(array, start, mid - 1)
	newNode.right = minHeightHelper(array, mid + 1, end)
	return newNode

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value) """
