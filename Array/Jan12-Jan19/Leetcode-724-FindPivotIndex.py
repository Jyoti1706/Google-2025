from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        right = total
        for i in range(len(nums)):
            right = right - nums[i]
            if left == right:
                return i
            left = left+nums[i]
        return -1



obj = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(obj.pivotIndex(nums)) # 3
nums = [1, 2, 3]
print(obj.pivotIndex(nums)) # -1
nums = [2,1,-1]
print(obj.pivotIndex(nums)) # 0
nums = [-1,-1,-1,-1,-1,0]
print(obj.pivotIndex(nums)) # 2
