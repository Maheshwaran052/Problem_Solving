function productOfArrayExecptSelf(nums) {
    let result = Array(nums.length).fill(1);
    let prefix = 1;

    for (let i = 0; i < nums.length; i++) {
        result[i] = prefix;
        prefix *= nums[i];
    }

    let postfix = 1;
    for (let i = nums.length - 1; i > -1; i--) {
        result[i] *= postfix;
        postfix *= nums[i];
    }
    return result
}


const nums = [1, 2, 3, 4]
console.log(productOfArrayExecptSelf(nums));