# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def isLeaf(self, node):
        return (node.left is None) and (node.right is None)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []

        # code here
        def solve(node, summ, path):
            if node is None:
                return
            if self.isLeaf(node) and summ == 0:
                # print(f"summ {summ}, path={path}")
                output.append(path)
                return
            if node.left:
                solve(node.left, summ - node.left.val, path + [node.left.val, ])
            if node.right:
                solve(node.right, summ - node.right.val, path + [node.right.val, ])

        if root:
            solve(root, targetSum - root.val, [root.val, ])
        return output
