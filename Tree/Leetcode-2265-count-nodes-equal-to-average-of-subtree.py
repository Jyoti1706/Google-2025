# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        output = [0, ]

        def Solve(node) -> int:
            if node is None:
                return (0, 0)

            Lval, Lcount = Solve(node.left)
            Rval, Rcount = Solve(node.right)
            summation = (Lval + Rval + node.val)
            length = (Rcount + Lcount + 1)
            avg = summation // length
            # print( node.val, avg, length)
            if avg == node.val:
                output[0] += 1
            # print(f"count: {output[0]}")
            return summation, length

        Solve(root)
        return output[0]

    def isLeaf(self, node):
        return (node.left is None) and (node.right is None)
