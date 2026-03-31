""" Algorithm

Initialize two pointers:

left = 0 (start of array)

right = n - 1 (end of array)

While left < right:

Calculate container area using
width = right - left
height = min(heights[left], heights[right]).

Update max_area if this area is larger.

Move the pointer with the smaller height:

If heights[left] < heights[right] → move left forward.

Otherwise → move right backward.

Continue until pointers meet.

Return max_area. """

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area = 0

        while(left<right):
            area = (right-left)*min(heights[left],heights[right])
            if(heights[left]<heights[right]):
                left+=1
            else:
                right-=1
            max_area=max(max_area,area)
        return max_area
            
        
        