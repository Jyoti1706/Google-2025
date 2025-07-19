from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths_via_Loop(self, root: Optional[TreeNode]) -> int:
        counter = [0 for _ in range(11)]
        result = [0]

        def solve(root):
            if not root:
                return
            counter[root.val] += 1
            if not root.left and not root.right:
                odd_freq = 0
                for i in range(1, 11):
                    if counter[i] % 2 != 0:
                        odd_freq += 1
                if odd_freq == 1:
                    result[0] += 1
            solve(root.left)
            solve(root.right)
            counter[root.val] -= 1

        solve(root)
        return result[0]

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        count = [0]
        result = [0]

        def solve(root, temp):
            if not root:
                return
            temp = temp ^ (1 << root.val)
            if not root.left and not root.right:
                if temp & temp-1 == 0:
                    result[0] += 1
            solve(root.left, temp)
            solve(root.right, temp)

        solve(root)
        return result[0]
