#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        result = ListNode()
        while l1.next and l2.next:
            result = ListNode(l1.val+l2.next)

