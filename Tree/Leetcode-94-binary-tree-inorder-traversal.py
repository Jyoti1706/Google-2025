# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        current = root
        result = []
        while current:
            if current.left is None:
                result.append(current.val) # Print when Left is None
                current = current.right # Move towards right
            else:
                left_child = current.left
                while left_child.right is not None:
                    left_child = left_child.right  ## go to rightest of that subtree
                left_child.right = current ## Link rightest to current
                temp = current
                current = current.left ## move towards left
                temp.left = None  ## remove link
        return result