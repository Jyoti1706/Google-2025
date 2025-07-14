# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
import math


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Top to bottom approach, pass min and max value along the path and at leafs return the abs difference
        and pass the max difference to up root back
        :param root:
        :return:
        """
        minV = math.inf
        maxV = -math.inf
        def solve(root, minV, maxV):
            if not root:
                return abs(maxV-minV)
            maxV = max(maxV, root.val)
            minV = min(minV, root.val)
            l = solve(root.left, minV, maxV)
            r = solve(root.right, minV, maxV)
            return max(l , r)
        return solve(root, minV, maxV)