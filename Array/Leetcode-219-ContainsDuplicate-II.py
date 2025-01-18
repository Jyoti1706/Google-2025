from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 1
        seen = {nums[i]: 0}
        while i < j < len(nums):
            if nums[j] in seen and abs(seen[nums[j]] - j) <= k:
                return True
            else:
                if abs(i - j) > k:
                    del seen[nums[i]]
                    seen[nums[j]] = j
                    i += 1
                    j += 1
                else:
                    seen[nums[j]]=j
                    j += 1
        return False

obj = Solution()
nums = [1,2,3,4,5,6,7]
k=3
print(obj.containsNearbyDuplicate(nums,k))

nums = [1,2,3,4,5,4,7]
k=3
print(obj.containsNearbyDuplicate(nums,k))

nums = [1,2,3,1,5,6,7]
k=2
print(obj.containsNearbyDuplicate(nums,k))