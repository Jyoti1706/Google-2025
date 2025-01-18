from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxArea = area if maxArea < area else maxArea
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            area = (right-left)*min(heights[left], heights[right])
            maxArea = area if maxArea < area else maxArea
        return maxArea

obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(obj.maxArea(height))
height = [1,1]
print(obj.maxArea(height))
