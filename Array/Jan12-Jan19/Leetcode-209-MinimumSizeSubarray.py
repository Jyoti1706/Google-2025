"""https://leetcode.com/problems/minimum-size-subarray-sum/description/


Given an array of positive integers nums and a positive integer target, return the minimal
length of a subarray  whose sum is greater than or equal to target. If there is no such subarray,
return 0 instead.

"""

import math


class Solution:
    def minSubArrayLen(self, target, nums):
        arraysum = -math.inf

        left = 0
        right = 1
        arraysum = 0
        currsum = nums[0]

        while left < right < len(nums):
            pass

