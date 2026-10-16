function moveZeroes(nums) {
    let left = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            // 1. Swap nums[i] and nums[left]
            if (i != left) {
                temp = nums[i];
                nums[i] = nums[left];
                nums[left] = temp;
            }
            // 2. Increment left
            left += 1;
        }
    }
    return nums;
}

let nums = [2, 1, 0, 3, 12, 0, 53, 0];
console.log(moveZeroes(nums));