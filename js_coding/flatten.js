
function flattenArray(nums) {
    const result = [];

    for (let i = 0; i < nums.length; i++) {
        if (Array.isArray(nums[i])) {
            const flattened = flattenArray(nums[i]);
            result.push(...flattened);
        } else {
            result.push(nums[i]);
        }
    }

    return result;
}


const nums = [1, [2, 3], [4, [5, 6]], 7];
console.log(flattenArray(nums));