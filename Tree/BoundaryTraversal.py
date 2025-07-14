"""
1. Collect Left Node
2. Collect Right Node
3. collect leave node
"""

from collections import deque


def is_leaf(node):
    return not node.left and not node.right


def boundary_traversal(root):
    if not root:
        return []
    res = []
    left = []
    right = []
    leaves = []

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        first, last = None, None
        level_node = []
        for i in range(level_size):
            node = queue.popleft()
            level_node.append(node)
            if i == 0:
                first = node
            if i == level_size - 1:
                last = node

            if is_leaf(node):
                leaves.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if first and not is_leaf(first) and first != root:
                left.append(first)
            if last and not is_leaf(last) and last != first:
                right.append(last)
            res.extend(left)
            res.extend(leaves)
            res.extend(reversed(right))

            return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class RecursionSolution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        1. left traversal
        2.  leaf node
        3. right side traversal
        """
        res = []
        if not root:
            return res
        if not self.isLeaf(root):
            res.append(root.val)
        self.leftBoundary(root.left, res)
        self.collectLeaf(root, res)
        self.collectRight(root.right, res)
        # print(res)
        return res

    def isLeaf(self, node):
        return True if node.left is None and node.right is None else False

    def leftBoundary(self, node, res):
        if node is None or self.isLeaf(node):
            return
        res.append(node.val)
        if node.left:
            self.leftBoundary(node.left, res)
        elif node.right:
            self.leftBoundary(node.right, res)

    ## Inorder Traversal for Leaves
    def collectLeaf(self, node, res):
        if node is None:
            return
        if self.isLeaf(node):
            res.append(node.val)
            return
        self.collectLeaf(node.left, res)
        self.collectLeaf(node.right, res)

    def collectRight(self, node, res):
        if node is None or self.isLeaf(node):
            return
        if node.right:
            self.collectRight(node.right, res)
        elif node.left:
            self.collectRight(node.left, res)
        res.append(node.val)
