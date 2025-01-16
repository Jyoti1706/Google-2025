import math
class Solution:
    def nextPermutation(self, arr):
        pivot = -1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        if pivot == -1:
            arr.sort()
            return
        nextbig = math.inf
        idx = -1
        for i in range(pivot+1, len(arr)):
            if arr[pivot] < arr[i] < nextbig:
                idx = i

        arr[idx], arr[pivot] = arr[pivot], arr[idx]
        arr[pivot+1:] = reversed(arr[pivot+1:])

obj = Solution()
arr = [2, 4, 1, 7, 5, 0]
obj.nextPermutation(arr)
print(arr)
# arr = [3, 4, 2, 5, 1]
# obj.nextPermutation(arr)
# print(arr)

arr = [3, 2,1]
obj.nextPermutation(arr)
print(arr)