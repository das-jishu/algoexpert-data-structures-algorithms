// O(n) time | O(n) space

//                      10
//                    5     15
//                  2   5       22
//                1

function inOrderTraverse(tree, array) {
  // [1, 2, 5, 5, 10, 15, 22]
  if (tree !== null) {
    inOrderTraverse(tree.left, array);
    array.push(tree.value);
    inOrderTraverse(tree.right, array);
  }
  return array;
}

function preOrderTraverse(tree, array) {
  // [10, 5, 2, 1, 5, 15, 22]
  if (tree !== null) {
    array.push(tree.value);
    preOrderTraverse(tree.left, array);
    preOrderTraverse(tree.right, array);
  }
  return array;
}

function postOrderTraverse(tree, array) {
  // [1, 2, 5, 5, 22, 15, 10]
  if (tree !== null) {
    postOrderTraverse(tree.left, array);
    postOrderTraverse(tree.right, array);
    array.push(tree.value);
  }
  return array;
}
