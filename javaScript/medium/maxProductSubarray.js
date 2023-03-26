/* 
LEETCODE PROBLEM: 

Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
*/

function maxProduct(nums) {
  let currentMaxProduct = nums[0];
  let currentMinProduct = nums[0];
  let result = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const num = nums[i];
    const tempMaxProduct = currentMaxProduct * num;

    currentMaxProduct = Math.max(tempMaxProduct, currentMinProduct * num, num);
    currentMinProduct = Math.min(tempMaxProduct, currentMinProduct * num, num);

    result = Math.max(result, currentMaxProduct);
  }

  return result;
}

const input = [-3, -5, -2, 100, -2];
const result = maxProduct(input);
console.log(result); // 6000
