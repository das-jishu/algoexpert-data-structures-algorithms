// Write a function that takes in a non-empty array of integers and returns the
// maximum sum that can be obtained by summing up all of the integers in a
// non-empty subarray of the input array. A subarray must only contain adjacent
// numbers (numbers next to each other in the input array).

// Sample input =  [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
// Sample output = 19  // [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]

function kadanesAlgorithm(array) {
  let maxEndingHere = array[0];
  let maxSoFar = array[0];

  for (let i = 1; i < array.length; i++) {
    const num = array[i];
    maxEndingHere = Math.max(maxEndingHere + num, num);
    maxSoFar = Math.max(maxSoFar, maxEndingHere);
  }

  return maxSoFar;
}

const input = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4];
const result = kadanesAlgorithm(input);
console.log(result); // 19
