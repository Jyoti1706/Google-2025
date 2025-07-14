class Solution:
    def subsets(self, nums):
        result = set()
        n = len(nums)
        def Solve(idx, curr ):
            if idx >= n:
                result.add(tuple(curr))
                return
            #print(type(curr))
            curr.append(nums[idx])
            Solve(idx+1,curr)
            curr.pop()
            Solve(idx+1, curr)
        curr = []

        Solve(0, curr)
        return list(result)

obj = Solution()
nums = [1,2,3]
print(obj.subsets(nums))