# Algorithm
""" 1. Create a hashmap and variable "needed" to store difference between nums list and target
2. If the needed value is in hashmap return its indices
3.else add the value to hashmap and continue """

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hashMap:
                return [hashMap[needed], i]
            hashMap[nums[i]] = i


nums = [1,3,4,5,4]
target = 9

sol = Solution()          # create object
res = sol.twoSum(nums,target)   # call method

print("RES:", res)
        