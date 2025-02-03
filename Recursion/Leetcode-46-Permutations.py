class Solution:
    def permute(self, nums):
        results = []
        self.findallPermutation(nums, 0, results)
        return results

    def findallPermutation(self, nums, idx, results):
        if idx == len(nums) - 1:
            results.append(nums.copy())

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.findallPermutation(nums, idx + 1,results)
            nums[i], nums[idx] = nums[idx], nums[i]


nums = [1, 2, 3, 4]
obj = Solution()
print(obj.permute(nums))
arr = "ABC"
print(obj.permute(arr))
