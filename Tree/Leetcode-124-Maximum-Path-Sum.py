from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [0]
        def Solve(root):
            if not root:
                return 0
            left = Solve(root.left)
            right = Solve(root.right)
            result[0] = max(result[0], left+right+root.val)
            return max(left, right)+ root.val
        Solve(root)
        return result[0]