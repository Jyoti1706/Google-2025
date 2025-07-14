from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(root):
            if root is None:
                return [True, 0]
            left_balanced, left_height = self.isBalanced(root.left)
            right_balanced, right_height = self.isBalanced(root.right)
            is_balanced = left_balanced and right_balanced and abs(left_height-right_height)<=1
            height = max(left_height, right_height)+1
            return [is_balanced, height]
        return solve(root)[0]