class Solution:
    def subsetSums(self, arr):
        n = len(arr)
        result = []
        def solve(idx, sum):
            if idx >= n:
                result.append(sum)
                return
            solve(idx+1, sum+arr[idx])
            solve(idx+1, sum)
        solve(0,0)
        return sorted(result)

obj = Solution()
arr = [2, 3]
print(obj.subsetSums(arr))