class Solution:
    def removeDuplicates(self, nums):

        right = 0
        left = 0
        prev = nums[left]
        while right < len(nums):
            if prev != nums[right]:
                prev = nums[right]
                left += 1
                nums[left] = nums[right]
            else:
                right += 1
        for i in range(left+1, len(nums)):
            nums[i] = "_"
        return nums

nums = [0,0,1,1,1,2,2,3,3,4]
obj = Solution()
print(obj.removeDuplicates(nums))