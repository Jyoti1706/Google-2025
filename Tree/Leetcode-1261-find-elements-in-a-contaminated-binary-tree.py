from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = set()
        def dfs(node, value):
            if not node:
                return
            node.val = value
            self.nodes.add(value)
            if node.left:
                dfs(node.left, 2*value+1)
            if node.right:
                dfs(node.right, 2*value+2)
        dfs(root,0)


    def find(self, target: int) -> bool:
        if target in self.nodes:
            return True