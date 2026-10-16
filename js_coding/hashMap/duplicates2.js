function haveDuplicates(nums, k) {
    let hashMap = new Map();

    for (let i = 0; i < nums.length; i++) {
        if (hashMap.has(nums[i])) {
            if (i - hashMap.get(nums[i]) <= k) {
                return true;
            }
        }
        hashMap.set(nums[i], i);
    }
    return false;
}

const numbers = [1, 2, 3, 1, 2, 3]
const k = 3
console.log(haveDuplicates(numbers, k))