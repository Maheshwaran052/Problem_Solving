""" Algorithm

Sort the array so that two-pointer technique can be used and duplicates can be skipped easily.

Traverse the array using index i (first element of triplet).

Skip duplicate values of nums[i] to avoid repeating triplets.

If nums[i] > 0, break because further numbers will also be positive (sum cannot be 0).

Use two pointers:

left = i + 1

right = n - 1

Calculate total = nums[i] + nums[left] + nums[right].

If total == 0

Add the triplet to result.

Skip duplicate values for left and right.

Move both pointers.

If total < 0

Move left forward to increase sum.

If total > 0

Move right backward to decrease sum.

Continue until left < right.

Return all unique triplets. """

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Optimization: if current number > 0, break
            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result