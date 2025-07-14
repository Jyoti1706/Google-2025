# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        # code here
        if not root:
            return []

        q = deque()
        hd_map = {}  # {hd: node.data}

        # queue holds pairs: (node, horizontal_distance)
        q.append((root, 0))

        while q:
            node, hd = q.popleft()

            # Only add the first node at each horizontal distance
            if hd not in hd_map:
                hd_map[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        # Return values sorted by horizontal distance
        return [hd_map[hd] for hd in sorted(hd_map)]
