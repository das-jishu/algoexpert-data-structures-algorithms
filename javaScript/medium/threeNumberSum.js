// O(n^2) time | O(n) space
function threeNumberSum(array, targetSum) {
  array.sort((a, b) => a - b);
  const triplets = [];
  const len = array.length;
  for (let i = 0; i <= len - 3; i++) {
    let left = i + 1;
    let right = len - 1;
    while (left < right) {
      const currSum = array[i] + array[left] + array[right];
      if (currSum === targetSum) {
        triplets.push([array[i], array[left], array[right]]);
        left++;
        right--;
      } else if (currSum > targetSum) {
        right--;
      } else if (currSum < targetSum) {
        left++;
      }
    }
  }
  return triplets;
}
