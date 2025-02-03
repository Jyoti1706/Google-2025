from typing import List


def findNSL(arr):
    n = len(arr)
    nse = [-1] * n
    stack = []
    for idx, num in enumerate(arr):
        while stack:
            if arr[stack[-1]] <= num:
                nse[idx] = stack[-1]
                stack.append(idx)
                break
            else:
                stack.pop()
        if not stack:
            stack.append(idx)
    return nse


def findNSR(arr):
    n = len(arr)
    nsr = [n] * n
    stack = []
    for idx in range(len(arr) - 1, -1, -1):
        while stack:
            if arr[stack[-1]] < arr[idx]:
                nsr[idx] = stack[-1]
                stack.append(idx)
                break
            else:
                stack.pop()
        if not stack:
            stack.append(idx)
    return nsr


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse = findNSL(arr)  # Next smaller to left
        pse = findNSR(arr)  # Next smaller to Right
        totalSum = 0
        mod = 1000000007
        n = len(arr)
        for i in range(0, n):
            left = i - nse[i]
            right = pse[i] - i
            totalWays = left * right
            total = arr[i] * totalWays
            totalSum = (totalSum + total) % mod
        return totalSum


obj = Solution()
arr = [11,81,94,43,3]
print(obj.sumSubarrayMins(arr))