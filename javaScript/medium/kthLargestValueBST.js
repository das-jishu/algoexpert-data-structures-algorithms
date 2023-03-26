class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Solution 1:
// O(n) time O(n) space
function findKthLargestValueInBst(tree, k) {
  const sortedNodeValues = [];
  inorderTraverse(tree, sortedNodeValues);
  return sortedNodeValues[sortedNodeValues.length - k];
}

function inorderTraverse(node, sortedNodeValues) {
  if (node === null) return;

  inorderTraverse(node.left, sortedNodeValues);
  sortedNodeValues.push(node.value);
  inorderTraverse(node.right, sortedNodeValues);
}

// Solution 2:
// O(h + k) time | O(h) space - where h is the height of the tree and k is the input parameter

class TreeInfo {
  constructor(numberOfNodesVisited, latestVisitedValue) {
    this.numberOfNodesVisited = numberOfNodesVisited;
    this.latestVisitedValue = latestVisitedValue;
  }
}

function findKthLargestValueInBst2(tree, k) {
  // Write your code here.
  const treeInfo = new TreeInfo(0, -1);
  reverseInorderTraverse(tree, treeInfo, k);
  return treeInfo.latestVisitedValue;
}

function reverseInorderTraverse(node, treeInfo, k) {
  if (node === null || treeInfo.numberOfNodesVisited >= k) {
    return;
  }
  reverseInorderTraverse(node.right, treeInfo, k);
  if (treeInfo.numberOfNodesVisited < k) {
    treeInfo.numberOfNodesVisited += 1;
    treeInfo.latestVisitedValue = node.value;

    reverseInorderTraverse(node.left, treeInfo, k);
  }
}

// Do not edit the lines below.
exports.BST = BST;
exports.findKthLargestValueInBst = findKthLargestValueInBst;
