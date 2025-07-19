
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, root, k):
        """
        time: o(n)
        Space: O(n/2*h)~ o(n*h)
        Optimization(Space): instead of storing path, check and add result
        :param root:
        :param k:
        :return:
        """
        paths = []
        result = set()
        temp = []
        def solve(node, temp):
            if not node:
                return
            temp.append(node)
            if not node.left and not node.right:
                paths.append(temp[:])
            solve(node.left, temp)
            solve(node.right, temp)
            temp.pop()
        solve(root, temp)
        for path in paths:
            #print(path)
            if len(path) > k:
                result.add(path[len(path)-k-1])
        return len(result)