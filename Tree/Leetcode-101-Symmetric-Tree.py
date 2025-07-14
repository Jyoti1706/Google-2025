class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        def isMirror(Node1, Node2):
            if not Node1 and not Node2:
                return True
            if not Node1 or not Node2:
                return False
            return Node1.val == Node2.val and isMirror(Node1.left, Node2.right) and isMirror(Node1.right, Node2.left)

        return isMirror(root.left, root.right)
