from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        ans = 0
        n = len(nums)
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1

            if suffix == 0:
                suffix = 1

            prefix = prefix*nums[i]
            suffix = suffix*nums[n-i-1]
            ans = max(ans, max(prefix,suffix))
        return ans

obj = Solution()
nums = [2,3,-2,4]
print(obj.maxProduct(nums))

nums = [-2,0,-1]
print(obj.maxProduct(nums))