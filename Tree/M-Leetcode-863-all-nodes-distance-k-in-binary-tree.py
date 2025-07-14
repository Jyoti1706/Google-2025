# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = {}
        ## Inorder traversal to map parent to child

        def inorder(root):
            if root is None:
                return
            if root.left:
                parentMap[root.left] = root
                inorder(root.left)
            if root.right:
                parentMap[root.right] = root
                inorder(root.right)
        inorder(root)

        visited = set()
        result = []
        def BFS(node, k, result):
            queue = [node]
            visited.add(node)
            while queue:
                length = len(queue)
                if k == 0:
                    break
                for _ in range(length):
                    current = queue.pop(0)
                    if current.left and (current.left not in visited):
                        queue.append(current.left)
                        visited.add(current.left)
                    if current.right and (current.right not in visited):
                        queue.append(current.right)
                        visited.add(current.right)
                    if parentMap.get(current,None) and (current.left not in visited):
                        queue.append(parentMap[current])
                        visited.add(parentMap[current])
                k -= 1
            while queue:
                current = queue.pop(0)
                result.append(current.val)

        BFS(target, k, result)
        return result



