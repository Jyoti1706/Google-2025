# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [(root,1)]
        output = []
        while queue:
            lvl = len(queue)
            temp = []
            for i in range(lvl):
                node, num = queue.pop(0)
                if node.left:
                    queue.append((node.left, num*2))
                    temp.append(num*2)
                if node.right:
                    queue.append((node.right, (num*2)+1))
                    temp.append((num * 2) + 1)
            output.append(temp)
        result = 0
        if len(output[-1]) > 1:
            result = output[-1][-1]-output[-1][0]+1
        else:
            result = 2
        return result

