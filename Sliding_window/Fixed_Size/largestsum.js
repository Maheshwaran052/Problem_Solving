/* 1. Let’s consider the array: [2, 1, 5, 1, 3, 2] and a window size of 3.

Initialization: Start with the first 3 elements: [2, 1, 5]. Calculate their sum: 2 + 1 + 5 = 8.
Slide the Window: Move the window one step to the right: [1, 5, 1]. Calculate the sum: 1 + 5 + 1 = 7.
Update and Evaluate: Compare the current sum (7) with the previous maximum sum (8). Since 8 is greater, keep the maximum sum as 8.
Slide the Window: Move the window again: [5, 1, 3]. Calculate the sum: 5 + 1 + 3 = 9.
Update and Evaluate: Compare the current sum (9) with the previous maximum sum (8). Update the maximum sum to 9.
Slide the Window: Continue sliding the window: [1, 3, 2]. Calculate the sum: 1 + 3 + 2 = 6.
Update and Evaluate: Compare the current sum (6) with the previous maximum sum (9). Since 9 is greater, the maximum sum remains 9.
Final Result: After sliding through all windows, the maximum sum found is 9. */

const maxSum = (arr, k) => {
    let max = 0;
    let windowSum = 0;

    // Total sum within the first window
    for (let i = 0; i < k; i++) {
        windowSum += arr[i];
    }
    max = windowSum; // initialize max with the first window sum

    // Slide the window
    for (let i = k; i < arr.length; i++) {
        windowSum += arr[i] - arr[i - k]; // new_sum = old_sum + new_element - old_element
        max = Math.max(max, windowSum);
    }

    return max;
}

let arr = [2, 1, 5, 1, 3, 2];
const maximum = maxSum(arr, 3);
console.log("MAXIMUM SUM:", maximum);





