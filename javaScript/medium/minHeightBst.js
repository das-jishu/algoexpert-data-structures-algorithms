// Construct Min height BST from a sorted Array where BST class with insert method is available;

// SOLUTION 1: O(nlog(n)) time | O(n) space

function minHeightBst(array) {
  return constructMinHeightBst(array, null, 0, array.length - 1);
}

function constructMinHeightBst(array, bst, leftIdx, rightIdx) {
  if (leftIdx > rightIdx) {
    return;
  }

  const midIdx = Math.floor((leftIdx + rightIdx) / 2);
  const valueToAdd = array[midIdx];

  if (bst === null) {
    bst = new BST(valueToAdd);
  } else {
    bst.insert(valueToAdd);
  }
  constructMinHeightBst(array, bst, leftIdx, midIdx - 1);
  constructMinHeightBst(array, bst, midIdx + 1, rightIdx);
  return bst;
}

// SOLUTION 2: O(n) time | O(n) space

function minHeightBst2(array) {
  // Write your code here.
  return constructMinHeightBst2(array, null, 0, array.length - 1);
}

function constructMinHeightBst2(array, bst, leftIdx, rightIdx) {
  if (rightIdx < leftIdx) {
    return;
  }

  const midIdx = Math.floor((leftIdx + rightIdx) / 2);
  const newBstNode = new BST(array[midIdx]);

  if (bst === null) {
    bst = newBstNode;
  } else {
    if (bst.value > array[midIdx]) {
      bst.left = newBstNode;
      bst = bst.left;
    } else {
      bst.right = newBstNode;
      bst = bst.right;
    }
  }

  constructMinHeightBst2(array, bst, leftIdx, rightIdx - 1);
  constructMinHeightBst2(array, bst, rightIdx + 1, rightIdx);
  return bst;
}

// SOLUTION 3: O(n) time | O(n) space - Cleaner

function minHeightBst3(array) {
  return constructMinHeightBst3(array, 0, array.length - 1);
}

function constructMinHeightBst3(array, leftIdx, rightIdx) {
  if (rightIdx < leftIdx) return;

  const midIdx = Math.floor((leftIdx + rightIdx) / 2);

  const bst = new BST(array[midIdx]);
  bst.left = constructMinHeightBst3(array, leftIdx, midIdx - 1);
  bst.right = constructMinHeightBst3(array, midIdx + 1, rightIdx);

  return bst;
}

// GIVEN BST class with insert() method:
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    if (value < this.value) {
      if (this.left === null) {
        this.left = new BST(value);
      } else {
        this.left.insert(value);
      }
    } else {
      if (this.right === null) {
        this.right = new BST(value);
      } else {
        this.right.insert(value);
      }
    }
  }
}
