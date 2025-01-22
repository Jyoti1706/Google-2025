from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalprod = 1
        zerocount = 0
        for n in nums:
            if n == 0:
                zerocount += 1
            finalprod = finalprod * n
        if zerocount > 1:
            return [0 for _ in nums]
        result = []
        for i, n in enumerate(nums):
            if n == 0:
                prod = 1
                for j, data in enumerate(nums):
                    if j != i:
                        prod = prod * data
            else:
                prod = finalprod // n
            result.append(prod)
        return result


obj = Solution()
nums=[1,2,3,4]
print(obj.productExceptSelf(nums))
nums=[-1,1,0,-3,3]
print(obj.productExceptSelf(nums))
