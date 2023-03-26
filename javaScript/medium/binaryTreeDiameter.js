// Space Complexity O(h), where h is the height of the tree
// Time Complexity O(n), where n is the number of nodes in the Binary tree
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function binaryTreeDiameter(tree) {
  // Write your code here.
  let diameter = 0;
  function dfsHeightCalculation(node) {
    if (!node) {
      return 0;
    }

    const leftHeight = dfsHeightCalculation(node.left, diameter);
    const rightHeight = dfsHeightCalculation(node.right, diameter);

    diameter = Math.max(diameter, leftHeight + rightHeight);

    return 1 + Math.max(leftHeight, rightHeight);
  }

  dfsHeightCalculation(tree);

  return diameter;
}
