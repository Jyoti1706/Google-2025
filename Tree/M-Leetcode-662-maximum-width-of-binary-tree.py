# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width = 0
        if root is None:
            return 0
        queue = deque()
        queue.append((root, 0))
        while queue:
            length = len(queue)
            left = queue[0][1]
            right = queue[length-1][1]
            width = max(width, right-left+1)
            for _ in range(length):
                currentNode, currentIdx = queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left, (currentIdx*2)+1)
                if currentNode.right:
                    queue.append(currentNode.left, (currentIdx*2)+2)
        return width


