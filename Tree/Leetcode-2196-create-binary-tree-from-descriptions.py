from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        hashmap = {}
        parents_set = set()
        for description in descriptions:
            root = description[0]
            child = description[1]
            branch = description[2]
            if root not in hashmap.keys():
                hashmap[root] = TreeNode(root)
            if child not in hashmap.keys():
                hashmap[root] = TreeNode(child)
            if branch == 1:
                hashmap[root].left = hashmap[child]
            else:
                hashmap[root].right = hashmap[child]
            parents_set.add(child)
        nodes = set(hashmap.keys())
        return nodes.difference(parents_set)