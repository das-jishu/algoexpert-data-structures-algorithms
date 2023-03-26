function invertBinaryTree(tree) {
  // Write your code here.
  if (!tree) {
    return;
  }

  swapLeftAndRight(tree);
  invertBinaryTree(tree.left);
  invertBinaryTree(tree.right);

  return tree;
}

function swapLeftAndRight(tree) {
  let tempNode = tree.left;
  tree.left = tree.right;
  tree.right = tempNode;
}

// This is the class of the input binary tree.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
