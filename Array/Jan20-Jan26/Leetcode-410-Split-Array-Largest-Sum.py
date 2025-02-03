from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        high = sum(nums)
        low = max(nums)
        while low <= high:
            mid = (low + high) // 2
            if self.isFeasible(nums, k, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

    def isFeasible(self, nums, k, mid):
        count = 1
        summation = 0
        for num in nums:
            if num + summation <= mid:
                summation += num
            else:
                count += 1
                summation = num
        return count <= k


obj = Solution()
nums = [7, 2, 5, 10, 8]
k = 2
print(obj.splitArray(nums,k))
nums = [1,2,3,4,5]
k = 2
print(obj.splitArray(nums,k))
