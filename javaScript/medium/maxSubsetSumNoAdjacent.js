// Dynamic Programming

// O(n) time | O(n) space
function maxSubsetSumNoAdjacent(array) {
  if (array.length === 0) return 0;

  let inc = array[0];
  let exc = 0;

  for (let i = 1; i < array.length; i++) {
    const newInc = array[i] + exc;
    const newExc = Math.max(inc, exc);

    inc = newInc;
    exc = newExc;
  }
  return Math.max(inc, exc);
}
