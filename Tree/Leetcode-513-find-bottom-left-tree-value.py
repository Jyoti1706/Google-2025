# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def findBottomLeftValue(self, root):
        path = self.levelOrder(root)
        return path[-1][0]
    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        output = []
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                current = queue.pop(0)
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            output.append(temp)
        return output


class Solution2:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = -1
        self.bottomLeftValue = 0
        self.dfs(root, 0)
        return self.bottomLeftValue

    def dfs(self, current: TreeNode, depth: int):
        if not current:
            return

        if depth > self.maxDepth:  # If true, we discovered a new level
            self.maxDepth = depth
            self.bottomLeftValue = current.val

        self.dfs(current.left, depth + 1)
        self.dfs(current.right, depth + 1)
        return



