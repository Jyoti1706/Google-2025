from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            i += 1
        i = n - 1
        right = n - 1
        while i > -1:
            if nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            i -= 1
        print(nums)


obj = Solution()
nums = [2, 0, 2, 1, 1, 0]
obj.sortColors(nums)
