class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)
        heights.append(0)

        for i in range(n+1):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                if(not stack):
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea,heights[index] * width)
            stack.append(i)
        return maxArea
            