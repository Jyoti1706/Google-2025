# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        hashmap = {}
        result = []
        def solve(root, hasmap, result):
            if not root:
                return "N"
            s = f"{str(root.val)},{solve(root.left, hashmap, result)},{solve(root.right, hasmap, result)}"
            if s in hasmap:
                result.append(root)
            else:
                hasmap[s] = 0
            hasmap[s] += 1
            return s
        solve(root,hashmap, result)
        return result
