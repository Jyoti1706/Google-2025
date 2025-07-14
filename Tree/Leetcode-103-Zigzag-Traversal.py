"""
BFS on Tree
Reverse odd index node list

"""
from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if not root:
            return []
        else:
            queue.append([root])
        i = 0
        while queue:
            current = queue[-1]
            temp = []
            for node in current:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if i % 2 == 0:
                queue.append(temp)
            else:
                queue.append(temp[::-1])
        return queue