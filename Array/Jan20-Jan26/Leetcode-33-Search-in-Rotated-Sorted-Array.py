from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = math.ceil((low + high) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid-1
        return -1


obj = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(obj.search(nums, target))  # 4
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(obj.search(nums, target))  # -1

nums = [1, 3, 5]
target = 5
print(obj.search(nums, target))  # 2

nums = [4, 1]
target = 4
print(obj.search(nums, target))  # 0
