from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
        return slow


obj = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(obj.removeElement(nums, val))
