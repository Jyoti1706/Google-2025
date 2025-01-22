from typing import List

import math


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        result = high
        while low <= high:
            mid = (low + high) // 2
            timetaken = self.getdays(weights, mid)
            if timetaken <= days:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result

    def getdays(self, weights, allowed):
        day = 0
        i = 0
        while i < len(weights):
            j = i
            sumW = 0
            while j < len(weights):
                sumW += weights[j]
                if sumW > allowed:
                    i+=1
                    break
                if weights[j] > allowed:
                    return len(weights)
                j += 1
            day += 1
            i = j
        return day


class NeetcodeSolution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res

obj = Solution()
# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5
# print(obj.shipWithinDays(weights, days))
weights = [1,2,3,1,1]
days = 4
print(obj.shipWithinDays(weights, days))
