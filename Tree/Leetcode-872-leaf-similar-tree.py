# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        str1 = ""
        str2 = ""

        def isLeaf(node):
            return (node.left is None) and (node.right is None)

        def inorder(node, result):
            if node is None:
                return result
            if isLeaf(node):
                result += str(node.val) + ","
            result = inorder(node.left, result)
            result = inorder(node.right, result)
            return result

        inorder(root1, str1)
        inorder(root2, str2)
        return str1 == str2
