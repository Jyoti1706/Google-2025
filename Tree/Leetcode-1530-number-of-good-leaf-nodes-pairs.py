# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        pair = 0
        def solve(node):
            nonlocal pair
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            Ldis = solve(node.left)
            Rdis = solve(node.right)
            for ld in Ldis:
                for rd in Rdis:
                    if ld+rd <= distance:
                        pair += 1
            depth = [d+1 for d in Ldis+Rdis if d+1 <= distance]
            return depth
        solve(root)
        return pair