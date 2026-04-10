from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Always binary search on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n

        left_part_size = (total + 1) // 2
        
        left, right = 0, m
        
        while left <= right:
            mid1 = (left + right) // 2

            #decides how many elements must be in left partition. Aim - Balance both partitions
            mid2 = left_part_size - mid1
            
            # Boundaries for nums1
            l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            r1 = nums1[mid1] if mid1 < m else float("inf")
            
            # Boundaries for nums2
            l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            r2 = nums2[mid2] if mid2 < n else float("inf")
            
            # Correct partition
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            
            # Move right -> left
            elif l1 > r2:
                right = mid1 - 1
            
            # Move left -> right
            else:
                left = mid1 + 1