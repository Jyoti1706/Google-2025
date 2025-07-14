# Definition for a binary tree node.
from typing import Optional

"""
Approach 1:
1. Create Parent MAP 
2. Initialize start node
3. Traverse Level Order and Parent MAP(BFS) and Visited to keep track of visited node
4. count time at each level

Approach 2:
1. Creat Graph 
2. BFS new graph +Visited 
3. count time at each level
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime_HashMap(self, root: Optional[TreeNode], start: int) -> int:
        """
        1. BFS and create parent map
        2. BFS using visited set, calculate time
        :param root:
        :param start:
        :return:
        """
        queue = [root]
        parent_map = {}
        start_node = [None,]
        def inorder(root):
            if root is None:
                return
            if root.left:
                parent_map[root.left] = root
                inorder(root.left)
            if root.right:
                parent_map[root.right] = root
                inorder(root.right)
            if root.val == start:
                start_node[0] = root
        inorder(root)


        # Step 2 BFS + Visited
        visited = set()
        queue = [start_node[0],]
        visited.add(start_node[0])
        time = 0
        while queue:
            length = len(queue)
            time += 1
            for _ in range(length):
                current_nodes = queue.pop(0)
                print(current_nodes.val)
                if current_nodes.left and (current_nodes.left not in visited):
                    queue.append(current_nodes.left)
                    visited.add(current_nodes.left)
                if current_nodes.right and current_nodes.right not in visited:
                    queue.append(current_nodes.right)
                    visited.add(current_nodes.right)
                parent = parent_map.get(current_nodes, None)
                if parent and parent not in visited:
                    queue.append(parent)
                    visited.add(parent)
        return time-1

    def amountOfTimeDFS(self, root: Optional[TreeNode], start: int) -> int:
        """
        Approach 2:
            1. Creat Graph
            2. BFS new graph +Visited
            3. count time at each level
        """
        result = [0]

        def solve(root, start):
            if root is None:
                return 0

            # Get distances from left and right subtrees
            LH = solve(root.left, start)
            RH = solve(root.right, start)

            # If current node is the start node
            if root.val == start:
                result[0] = max(LH, RH)
                return -1  # Signal that start node was found

            # If start node is in left subtree
            elif LH >= 0 and RH >= 0:
                # Start node not found in either subtree
                return max(LH, RH) + 1

            else:
                # Start node found in one of the subtrees
                # Calculate distance through current node
                dis = abs(LH) + abs(RH)
                result[0] = max(dis, result[0])
                return min(LH, RH) - 1  # Propagate distance upward

        solve(root,start)
        return result[0]


A = TreeNode(1)
B = TreeNode(5)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(10)
F = TreeNode(6)
G = TreeNode(9)
H = TreeNode(2)

A.left = B
A.right = C
B.right = D
D.left = G
D.right = H
C.left = E
C.right = F

obj = Solution()
print(obj.amountOfTimeDFS(A, C))
