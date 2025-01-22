from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums)==0:
            return 0
        longest = 1
        for num in iter(nums):
            if num-1 in nums:
                continue
            else:
                count =1
                while True:
                    if num+1 in nums:
                        count += 1
                        num = num+1
                    else:
                        break
                longest = max(longest,count)
        return longest





obj= Solution()
nums = [100,4,200,1,3,2]
print(obj.longestConsecutive(nums))
nums = [0,3,7,2,5,8,4,6,0,1]
print(obj.longestConsecutive(nums))