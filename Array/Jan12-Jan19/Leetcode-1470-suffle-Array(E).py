from typing import List


class Solution:
    def shuffle1(self, nums: List[int], n: int) -> List[int]:
        start = 0
        mid = n
        output=[]
        length = 2*n
        while start < n and mid < length:
            output.append(nums[start])
            output.append(nums[mid])
            start += 1
            mid += 1
        return output

    def shuffle(self, nums: List[int], n: int) -> List[int]:

        return list(zip(nums[:n], nums[n:]))