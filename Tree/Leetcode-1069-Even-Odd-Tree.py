from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        hashmap = {}
        evenPassed=True
        oddPassed = True
        def solve(root, level):

            nonlocal evenPassed, oddPassed
            if not oddPassed or not evenPassed:
                return False
            if not root:
                return True
            if level%2 == 0:
                prev = hashmap.get(level, -math.inf)
                if root.val > prev and root.val%2 != 0:
                    hashmap[level] = root.val
                else:
                    evenPassed = False
            else:
                prev = hashmap.get(level, math.inf)
                if root.val < prev and root.val%2 == 0:
                    hashmap[level] = root.val
                else:
                    oddPassed  = False
            return solve(root.left, level+1) & solve(root.right, level+1) & oddPassed & evenPassed
        return solve(root, 0 )
