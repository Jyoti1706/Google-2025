# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        levels = {}
        heights = {}
        LFirstMaxs = {}
        LSecondMaxs = {}

        def findHeight(root, level):
            if not root:
                return 0
            levels[root.val] = level
            heights[root.val] = max(findHeight(root.left, level + 1), findHeight(root.right, level + 1)) + 1
            if LFirstMaxs.get(level, 0) < heights[root.val]:
                LSecondMaxs[level] = LFirstMaxs.get(level, 0)
                LFirstMaxs[level] = heights[root.val]
            elif LSecondMaxs.get(level, 0) < heights[root.val]:
                LSecondMaxs[level] = heights[root.val]
            return heights[root.val]

        findHeight(root, 0)
        result = []
        for query in queries:
            l = levels[query]
            if LFirstMaxs[l] == heights[query]:
                result.append(LSecondMaxs[l] + l - 1)
            else:
                result.append(LFirstMaxs[l] + l - 1)
        return result
