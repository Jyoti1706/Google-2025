from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        zerorow = set()
        zerocol = set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zerorow.add(r)
                    zerocol.add(c)
        for r in iter(zerorow):
            for c in range(col):
                matrix[r][c] = 0
        for c in iter(zerocol):
            for r in range(row):
                matrix[r][c] = 0

