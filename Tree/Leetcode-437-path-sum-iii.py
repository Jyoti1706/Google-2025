from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    https://leetcode.com/problems/path-sum-iii/

    Prefix_Sum + DFS

    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        hashmap = {0: 1}

        def Solve(node, run_sum, target, hashmap):
            if not node:
                return 0
            run_sum += node.val
            count = hashmap.get( run_sum-target, 0)
            hashmap[run_sum] = hashmap.get(run_sum, 0) + 1

            count += Solve(node.left, run_sum, target, hashmap) + Solve(node.right, run_sum, target, hashmap)
            hashmap[run_sum] -= 1
            return count

        return Solve(root, 0, targetSum, hashmap)
