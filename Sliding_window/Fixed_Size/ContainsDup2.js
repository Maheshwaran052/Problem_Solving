/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    var set = new Set();
    for(let winSize=0; winSize<nums.length;winSize++)
    {
        if(winSize > k )
        {
        set.delete(nums[winSize-k-1])
        }
        if(set.has(nums[winSize]))
        {
            return true;
        }
        set.add(nums[winSize]);
    }
  return false;
};