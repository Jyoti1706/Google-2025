from typing import Optional, List
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        hashmap = defaultdict(list)
        hashmap[0].append(root.val)
        queue.append((root, 0))
        while queue:
            length = len(queue)
            for i in range(length):
                node, distance = queue.popleft()
                level_hm = defaultdict(list)
                if node.left:
                    queue.append((node.left, distance - 1))
                    level_hm[distance - 1].append(node.left.val)
                if node.right:
                    queue.append((node.right, distance + 1))
                    level_hm[distance + 1].append(node.right.val)
            for k, v in level_hm:
                hashmap[k].extend(v.sort())
        hashmap = dict(sorted(hashmap.items()))
        result = []
        for k, v in hashmap.items():
            result.append(v)
        return result

    def verticalTraversal_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        distance = {}

        def solve(node, dis):
            if root is None:
                return
            if dis in distance.keys():
                distance[dis].append(node.val)
            else:
                distance[dis] = [node.val, ]
            solve(node.left, dis - 1)
            solve(node.right, dis + 1)

        solve(root, 0)
        hashmap = dict(sorted(distance.items()))
        result = []
        for k, v in hashmap.items():
            result.append(v)
        return result
