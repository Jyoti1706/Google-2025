from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            withoutFlip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            withFlip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
            return withoutFlip or withFlip
        return False