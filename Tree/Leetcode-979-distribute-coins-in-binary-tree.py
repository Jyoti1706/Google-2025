from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = [0, ]

        def Solve(node):
            if not node:
                return 0
            left = Solve(node.left)
            right = Solve(node.right)
            moves[0] += abs(left)+abs(right)
            return left+right+node.val-1
        Solve(root)
        return moves[0]