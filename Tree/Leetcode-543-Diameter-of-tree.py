# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root is None:
                return 0
            left = solve(root.left)
            right = solve(root.right)
            result[0] = max(result[0], left + right) # Edge count not root count
            return max(left, right) + 1

        result = [0]
        solve(root)
        return result[0]
