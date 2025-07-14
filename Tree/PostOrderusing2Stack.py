from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack1 = []
        stack2 = []
        if root is None:
            return []
        stack1.append(root)
        while stack1:
            current = stack1.pop()
            stack2.append(current.val)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        return stack2[::-1]