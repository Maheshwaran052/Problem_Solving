function twoSum(nums, target) {
    const hashMap = new Map();
    for (let i = 0; i < nums.length; i++) {
        const needed = target - nums[i];
        if (!hashMap.has(needed)) {
            hashMap.set(nums[i], i)
        }
        else {
            return [hashMap.get(needed), i]
        }

    }
}

const nums = [2, 7, 11, 15];
const target = 22;
const result = twoSum(nums, target)
console.log(result);