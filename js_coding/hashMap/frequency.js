function frequency(nums) {
    freqMap = new Map();
    for (const num of nums) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }
    return freqMap
}



const nums = [1, 2, 2, 3, 3, 3, 4];
result = frequency(nums)
console.log(result)