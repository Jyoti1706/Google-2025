from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            last = nums[-1]
            for i in range(len(nums) - 2,-1,-1):
                nums[i + 1] = nums[i]
            nums[0] = last
            k -= 1
        print(nums)


obj = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
obj.rotate(nums,k)