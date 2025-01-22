from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for num in nums:
            data[num] = data.get(num, 0)-1
        data = list(zip(data.values(),data.keys()))
        heapq.heapify(data)
        results = []
        while k > 0:
            results.append(heapq.heappop(data)[1])
            k -= 1
        return results

obj = Solution()
nums = [1,1,1,2,2,3]
k=2
print(obj.topKFrequent(nums,k))
nums = [3,0,1,0]
k = 1
print(obj.topKFrequent(nums,k))