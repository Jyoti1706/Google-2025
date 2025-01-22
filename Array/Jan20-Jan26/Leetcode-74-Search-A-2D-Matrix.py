from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_idx = 0
        col = len(matrix)
        low = 0
        high = col-1
        while low <= high:
            mid = (low+high)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0] > target:
                high = mid-1
            else:
                low = mid+1
        row = len(matrix[0])
        start_idx = mid if matrix[mid][0] <= target <= matrix[mid][row] else mid-1
        low = 0
        high = len(matrix[start_idx])-1
        while low <= high:
            mid = (low + high) // 2

            if matrix[start_idx][mid] == target:
                return True
            elif matrix[start_idx][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

obj = Solution()
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
# print(obj.searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 11
print(obj.searchMatrix(matrix, target))
