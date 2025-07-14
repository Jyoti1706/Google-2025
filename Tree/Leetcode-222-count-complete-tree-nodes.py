# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getLeftHeight(root):
    if not root:
        return 0
    lh = 0
    temp = root
    while temp:
        temp = temp.left
        lh += 1
    return lh


def getRightHeight(root):
    if not root:
        return 0
    rh = 0
    temp = root
    while temp:
        temp = temp.right
        rh += 1
    return rh


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lh = getLeftHeight(root)
        rh = getRightHeight(root)
        if lh == rh:
            return pow(2, lh)-1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
