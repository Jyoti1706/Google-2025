# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxP = [0,]

        def treeSum(self, root):
            if not root:
                return 0
            left = self.treeSum(root.left)
            right = self.treeSum(root.right)
            summation = root.val + left + right
            maxP[0] = max(maxP[0], (totalsum)-summation*summation)
            return summation

        totalsum = treeSum(root)
        treeSum(root)
        return maxP


