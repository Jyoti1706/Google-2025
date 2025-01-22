from typing import List

import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = high
        while low <= high:
            mid = (low + high) // 2
            timeRequired = sum([math.ceil(pile / mid) for pile in piles])
            if timeRequired <= h:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result


obj = Solution()
piles = [3, 6, 7, 11]
h = 8
print(obj.minEatingSpeed(piles, h))
piles = [30, 11, 23, 4, 20]
h = 6
print(obj.minEatingSpeed(piles, h))
piles = [30,11,23,4,20]
h = 5
print(obj.minEatingSpeed(piles, h))
