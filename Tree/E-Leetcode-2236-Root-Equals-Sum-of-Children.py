from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if (root is None) or (root.left is None and root.right is None):
            return True
        childsum = 0
        if root.left:
            childsum += root.left.val
        if root.right:
            childsum += root.right.val

        return childsum == root.val and self.checkTree(root.left) and self.checkTree(root.right)