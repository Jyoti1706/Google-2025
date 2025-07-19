# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = ""
        mapping = {i: chr(ord('a') + i) for i in range(26)}

        def solve(node, current):
            nonlocal result
            if not node:
                return
            current = mapping[node.val] + current
            if not node.left and not node.right:
                if result == "" or current < result:
                    result = current
                return

            solve(node.left, current)
            solve(node.right, current)

        solve(root, "")
        return result
