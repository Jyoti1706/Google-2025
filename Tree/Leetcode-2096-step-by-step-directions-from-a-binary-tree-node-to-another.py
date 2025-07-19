from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_lowest_common_ancestor(self, root, nodeA, nodeB):
        if not root:
            return None
        if root.val == nodeA or root.val == nodeB:
            return root
        left = self.get_lowest_common_ancestor(root.left, nodeA, nodeB)
        right = self.get_lowest_common_ancestor(root.right, nodeA, nodeB)

        if left and right:
            return root

        return left if left else right

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        lca_node = self.get_lowest_common_ancestor(root, startValue, destValue)

        lcaToSrc = []
        lcaToDest = []

        def findPath(node: TreeNode, target: int, path: List):
            if node is None:
                return False
            if node.val == target:
                return True
            path.append("L")
            if findPath(node.left, target, path):
                return True
            path.pop()
            path.append("R")
            if findPath(node.right, target, path):
                return True
            path.pop()
            return False

        findPath(lca_node, startValue, lcaToSrc)
        findPath(lca_node, destValue, lcaToDest)
        # Step 3: Convert path_to_start into 'U's
        return "U" * len(lcaToSrc) + "".join(lcaToDest)
