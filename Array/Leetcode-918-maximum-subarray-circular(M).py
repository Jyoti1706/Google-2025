from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 1. Find total sum
        total = sum(nums)
        """
        maxsum can be from within array (kadanes max)
        max sum can be from circular max sum, in this case find minsum within array 
        so total-minsum = circular_maxsum
        """
        maxsum = self.kadanesMax(nums)
        minsum = self.kadanesMin(nums)

        result = max(total-minsum, maxsum) if maxsum > 0 else minsum
        return result
    def kadanesMax(self, nums):
        maxsum = nums[0]
        cursum = 0
        for num in nums:
            cursum = num if cursum < 0 else cursum+num
            maxsum = cursum if cursum > maxsum else maxsum
        return maxsum

    def kadanesMin(self, nums):
        minsum = nums[0]
        cursum = 0
        for num in nums:
            cursum = num if cursum > 0 else cursum+num
            minsum = cursum if cursum < minsum else minsum
        return minsum


obj = Solution()
nums = [5,1,2,-11,5]
print(obj.maxSubarraySumCircular(nums))
nums = [1,-2,3,-2]
print(obj.maxSubarraySumCircular(nums))
nums = [5,-3,5]
print(obj.maxSubarraySumCircular(nums))
