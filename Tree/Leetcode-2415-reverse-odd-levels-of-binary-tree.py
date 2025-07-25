from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        while q:
            if level&1:
                l, r = 0 , len(q)-1
                while l<r:
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.right)
                if node.right:
                    q.append(node.left)
            level += 1
        return root
