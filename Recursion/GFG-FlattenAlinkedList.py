# User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''


def mergeTwoList(L1, L2):
    if not L1:
        return L2
    if not L2:
        return L1
    result = ""
    if L1.data < L2.data:
        result = L1
        result.bottom = mergeTwoList(result.bottom, L2)
    else:
        result = L2
        result.bottom = mergeTwoList(L1, result.bottom)
    return result


class Solution:
    def flatten(self, head):
        if head is None:
            return None
        head2 = self.flatten(head.next)
        return mergeTwoList(head, head2)
