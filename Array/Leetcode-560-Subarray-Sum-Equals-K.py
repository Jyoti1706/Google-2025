from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        prefixSums = {0: 1}
        for n in nums:
            currsum += n
            diff = currsum - k
            res += prefixSums.get(diff, 0)
            prefixSums[diff] = prefixSums.get(diff, 0) + 1
        return res


obj = Solution()
# nums = [1, 2, 3]
# print(obj.subarraySum(nums, k=3))

obj = Solution()
nums = [1, 1, 1]
print(obj.subarraySum(nums, k=2))
