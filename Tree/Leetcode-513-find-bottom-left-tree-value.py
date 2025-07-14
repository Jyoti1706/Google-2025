# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
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

