from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        right = 0
        size = len(nums1)+len(nums2)-1
        if size % 2 == 0:
            median = [size//2]
        else:
            median = [size // 2, (size//2)+1]
