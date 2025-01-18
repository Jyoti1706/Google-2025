import math


class Solution:
    def maxTurbulenceSize(self, arr):
        if len(arr) == 1:
            return 1

        sym_arr = []
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                sym_arr.append("<")
            elif arr[i - 1] > arr[i]:
                sym_arr.append(">")
            else:
                sym_arr.append("=")
        prev = None
        count = 0
        maxpair = -math.inf
        for sym in sym_arr:
            if prev is None and sym != "=":
                prev = sym
                count = 1
                continue
            if sym == prev:
                maxpair = count if count > maxpair else maxpair
                count = 1
            elif sym == "=":
                maxpair = count if count > maxpair else maxpair
                prev = None
                count = 0
            else:
                count += 1
                prev = sym
        return (count if count > maxpair else maxpair) + 1

    def maxTurbulenceSizeSL(self, arr):
        l , r = 0, 1
        res, prev = 1, ""
        while r < len(arr):
            if arr[r-1]> arr[r] and prev != ">":
                res = max(res, r-l+1)
                r += 1
                prev = ">"
            elif arr[r-1] <  arr[r] and prev != "<":
                res = max(res, r-l+1)
                r += 1
                prev = "<"
            else:
                r = r+1 if arr[r] == arr[r-1] else r
                l = r-1
                prev = ""
        return res



obj = Solution()
# arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
# print(obj.maxTurbulenceSize(arr))
# arr = [6, 9, 4, 2, 10, 7, 8, 8, 1, 9]
# print(obj.maxTurbulenceSize(arr))
# arr = [4,8,12,16]
# print(obj.maxTurbulenceSize(arr))
# arr = [4]
# print(obj.maxTurbulenceSize(arr))
# arr = [4,4,4,4,4]
arr = [0,8,45,88,48,68,28,55,17,24]
print(obj.maxTurbulenceSize(arr))
