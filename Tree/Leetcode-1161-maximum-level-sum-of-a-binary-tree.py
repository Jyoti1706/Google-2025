# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        queue = [root,]
        level = 0
        result = [root.val, level]
        while queue:
            n = len(queue)
            level += 1
            level_sum = 0
            for _ in range(n):
                v = queue.pop(0)
                level_sum += v
            if level_sum > result[0]:
                result = [level_sum, level]
        return result[1]