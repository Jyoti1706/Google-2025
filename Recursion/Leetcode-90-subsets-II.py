from typing import List


class Solution:
    def subsetsWithDupNaive(self, nums: List[int]) -> List[List[int]]:
        """
        Approach:
        1. Create Subsets
        2. sort the subset and then append the result to set (convert to tuple)
        :param nums:
        :return:
        """
        result = set()
        n = len(nums)

        def Solve(idx, curr):
            if idx >= n:
                result.add(tuple(sorted(curr)))
                return
            # print(type(curr))
            curr.append(nums[idx])
            Solve(idx + 1, curr)
            curr.pop()
            Solve(idx + 1, curr)

        curr = []

        Solve(0, curr)
        return sorted(list(result))

    def subsetsWithDupOptimal(self, nums):
        """
        Sort the array to ensure that duplicates appear consecutively.
        Use backtracking to explore subsets, skipping duplicate elements at each recursion level.
        Use an index to track the current element and avoid duplicates by skipping them.
        :param nums:
        :return:
        """
        res = []
        nums.sort()  # Sort to handle duplicates

        def backtrack(start, path):
            res.append(path[:])  # Store a copy of the path

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Backtrack

        backtrack(0, [])
        return res



nums = [4,4,4,1,4]
obj = Solution()
print(obj.subsetsWithDupOptimal(nums))
print(obj.subsetsWithDupNaive(nums))