# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        width = 0
        queue = deque()
        queue.append([root, 0])
        while queue:
            current_level = queue.popleft()
            left = current_level[0][1]
            right = current_level[-1][1]
            width = max(width, right-left+1)
            temp = []
            for node, idx in current_level:
                if node.left:
                    temp.append([node.left, 2*idx+1])
                if node.right:
                    temp.append([node.right, 2*idx+2])
            if len(temp) > 0:
                queue.append(temp)
        return width