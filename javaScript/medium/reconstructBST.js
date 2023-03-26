// This is an input class. Do not edit.
class BST {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(value) {
    const newNode = new BST(value);
    if (this.root === null) {
      this.root = newNode;
    } else {
      let currentNode = this.root;

      while (true) {
        if (value < currentNode.value) {
          if (!currentNode.left) {
            currentNode.left = newNode;
            return this;
          }
          currentNode = currentNode.left;
        } else {
          if (!currentNode.right) {
            currentNode.right = newNode;
            return this;
          }
          currentNode = currentNode.right;
        }
      }
    }
  }
}

function reconstructBst(preOrderTraversalValues) {
  // Write your code here.
  let tree = new BinarySearchTree();

  for (let i = 0; i < preOrderTraversalValues.length; i++) {
    tree.insert(preOrderTraversalValues[i]);
  }

  return tree.root;
}

const preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18];
reconstructBst(preOrderTraversalValues);
