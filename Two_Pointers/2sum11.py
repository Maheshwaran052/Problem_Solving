from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers)-1
        left = 0

        while left <= right:
            needed = numbers[left] + numbers[right]
            if(needed == target):
                return [left+1,right+1]
            elif(needed > target):
                right-=1
            else:
                left+=1
        return []
        