// SOLUTION 1:
// O(n) time | O(n) space
function twoNumberSum(array, targetSum) {
  let obj = {};

  for (let x of array) {
    if (obj[targetSum - x]) {
      return [targetSum - x, x];
    } else {
      obj[x] = true;
    }
  }

  return [];
}

// SOLUTION 2:
// O(nlog(n)) | O(1) space
function twoNumberSum(array, targetSum) {
  let obj = {};

  for (let x of array) {
    if (obj[targetSum - x]) {
      return [targetSum - x, x];
    } else {
      obj[x] = true;
    }
  }

  return [];
}
