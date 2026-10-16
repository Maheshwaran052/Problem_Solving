function maxSubarraySum(nums, k) {
    let windowSum = 0;

    for (let i = 0; i < k; i++) {
        windowSum += nums[i];
    }
    let maxSum = windowSum;

    for (let i = k; i < nums.length; i++) {
        windowSum += nums[i] - nums[i - k];
        maxSum = Math.max(maxSum, windowSum);
    }
    return maxSum;
}

const nums = [2, 1, 5, 1, 3, 2];
const k = 3;
console.log(maxSubarraySum(nums, k));