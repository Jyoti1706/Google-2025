from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        result = set()

        def backtracking(idx, target, current):
            if target == 0:
                result.add(tuple(sorted(current)))
            if idx >= n:
                return
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:  # Skip duplicates
                    continue
                if candidates[i] > target:
                    break
                current.append(candidates[i])
                backtracking(i + 1, target - candidates[i], current)
                current.pop()

        backtracking(0, target, [])
        return list(result)


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
obj = Solution()
print(obj.combinationSum2(candidates, target))
candidates = [2,5,2,1,2]
target = 5
print(obj.combinationSum2(candidates, target))