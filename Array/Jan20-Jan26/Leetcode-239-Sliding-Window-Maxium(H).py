"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the
very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums, k):
        ## Use Monotonic
        dq = []
        results = []
        for i in range(len(nums)):
            while len(dq) != 0 and dq[0] <= i-k:
                dq.pop(0)
            while len(dq) != 0 and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                results.append(nums[dq[0]])
        return results
obj = Solution()
# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# print(obj.maxSlidingWindow(nums, k))
# nums = [1]
# k = 1
# print(obj.maxSlidingWindow(nums, k))
#
# nums =[1,-1]
# k =1
# print(obj.maxSlidingWindow(nums, k))
nums = [9,10,9,-7,-4,-8,2,-6]
print(obj.maxSlidingWindow(nums, k=5))
