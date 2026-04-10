from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                # min in right
                low = mid + 1
            

            elif nums[mid] < nums[high]:
                # min in left (including mid)
                high = mid

            else:
                # nums[mid] == nums[high]
                # cannot decide → shrink
                high -= 1

        return nums[low]