from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = set()

        def backtrack(idx, target, curr):
            if idx >= n or target < 0:
                return
            if target == 0:
                result.add(tuple(curr.copy()))
                return
            #pick
            if candidates[idx] <= target:
                curr.append(candidates[idx])
                backtrack(idx, target - candidates[idx], curr)
                curr.pop()
            backtrack(idx+1, target, curr)
        backtrack(0, target, [])
        return list(result)

obj = Solution()
candidates = [2,2,3,4,7]
print(obj.combinationSum(candidates, target=7))

