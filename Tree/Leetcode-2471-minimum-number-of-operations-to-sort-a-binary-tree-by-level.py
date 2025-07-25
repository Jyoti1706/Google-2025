from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimum_swap_at_level(self, level_array):
        mp = {val: idx for idx, val in enumerate(level_array)}
        sorted_array = sorted(level_array)
        swaps = 0
        for idx in range(len(level_array)):

            if level_array[idx] == sorted_array[idx]:
                continue

            curr_idx = mp[sorted_array[idx]]
            mp[level_array[curr_idx]] = idx
            mp[level_array[idx]] = curr_idx
            level_array[curr_idx], level_array[idx] = level_array[idx], level_array[curr_idx]
            swaps += 1
        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        result = 0
        while queue:
            level_array = []
            for _ in range(len(queue)):
                current = queue.popleft()
                level_array.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result += self.minimum_swap_at_level(level_array)
        return result
