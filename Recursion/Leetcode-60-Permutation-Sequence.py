import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ""
        fact = math.factorial(n)
        nums = [i for i in range(1, n+1)]

        def solve(n, k, nums, fact, result):

            if len(nums) == 0:
                return result
            else:
                fact = fact // n
                idx = k // fact
                k = k % fact
                result += str(nums[idx])
                nums.pop(idx)
                return solve(n - 1, k, nums, fact, result)

        return solve(n, k-1, nums, fact, result)


obj = Solution()
print(obj.getPermutation(4, 9))  # 2314
print(obj.getPermutation(3, 1))  # 123
print(obj.getPermutation(3, 3))  # 213
