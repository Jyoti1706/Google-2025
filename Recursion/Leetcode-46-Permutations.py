from typing import List


class Solution_old:
    def permute(self, nums):
        results = []
        self.findallPermutation(nums, 0, results)
        return results

    def findallPermutation(self, nums, idx, results):
        if idx == len(nums) - 1:
            results.append(nums.copy())

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.findallPermutation(nums, idx + 1, results)
            nums[i], nums[idx] = nums[idx], nums[i]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def Recursion(nums):
            result = []
            if len(nums) == 1:
                return [nums.copy()]
            for i in range(len(nums)):
                n = nums.pop(0)
                perms = Recursion(nums)
                for perm in perms:
                    perm.append(n)
                result.extend(perms)
                nums.append(n)
            return result

        return Recursion(nums)


nums = [1, 2, 3]
obj = Solution()
print(obj.permute(nums))
