from typing import List
import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        diffarray = []
        for idx, num in enumerate(arr):
            heapq.heappush(diffarray, (abs(x - num), idx))
        result = []
        for i in range(k):
            min_element, idx = heapq.heappop(diffarray)
            result.append((idx, arr[idx]))
        result.sort(key=lambda y: y[1])
        print(result)
        return [data[1] for data in result]


obj = Solution()
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(obj.findClosestElements(arr, k, x))
arr = [1, 1, 2, 3, 4, 5]
k = 4
x = -1
print(obj.findClosestElements(arr, k, x))
