from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        boat = 0
        while left <= right:
            if people[right]+people[left] <= limit:
                boat += 1
                right -= 1
                left += 1
            elif people[right]<=limit:
                boat += 1
                right -= 1
            else:
                boat += 1
                left += 1
        return boat

obj = Solution()
people = [3,2,2,1]
limit = 3
print(obj.numRescueBoats(people, limit))