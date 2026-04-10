from typing import List

class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            if nums[low] <= nums[high]:
                return low

            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return low

    def binarySearch(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def searchWithRotation(self, nums: List[int], target: int):
        rot = self.findMinIndex(nums)

        if target >= nums[0]:
            idx = self.binarySearch(nums, 0, rot - 1, target)
        else:
            idx = self.binarySearch(nums, rot, len(nums) - 1, target)

        return rot, idx


nums = [3,4,5,6,0,1]
target = 6

sol = Solution()
print(sol.searchWithRotation(nums, target))  # (4, 3)