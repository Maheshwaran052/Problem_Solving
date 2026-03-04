/* 2. Variable Size Sliding Window:

The general steps to solve these questions by following below steps:

In this type of sliding window problem, we increase our right pointer one by one till our condition is true.
At any step if our condition does not match, we shrink the size of our window by increasing left pointer.
Again, when our condition satisfies, we start increasing the right pointer and follow step 1.
We follow these steps until we reach to the end of the array. */


//Example Problem: Longest Subarray with Sum Less Than K

const maxSubArrayLength = (arr, k) => {
    let maxLength = 0;
    let left = 0;
    let windowSum = arr[0];

    for (let right = 1; right < arr.length; right++) {
        // Add new element to window
        windowSum += arr[right];

        // Shrink window from left while sum >= k
        while (windowSum >= k && left <= right) {
            windowSum -= arr[left];
            left++;
        }

        // Update maxLength
        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
}

let arr = [1, 2, 3, 4, 5,1,1,1,1,1,1,1,1];
let k = 14;
let maxLength = maxSubArrayLength(arr, k);
console.log("MAX LENGTH:", maxLength);
