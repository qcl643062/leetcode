"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        stack = []
        if l1.val >= l2.val:
            l = l2
            stack = [l1, l2.next]
        else:
            l = l1
            stack = [l1.next, l2]
        left = l
        while True:
            if not stack[0]:
                left.next = stack[1]
                return l
            if not stack[1]:
                left.next = stack[0]
                return l
            if stack[0].val >= stack[1].val:
                left.next = stack[1]
                left = left.next
                stack[1] = stack[1].next
            else:
                left.next = stack[0]
                left = left.next
                stack[0] = stack[0].next
s = Solution()
m = s.mergeTwoLists(ListNode(1,ListNode(2, ListNode(3))), ListNode(2))
while m:
    print m.val
    m = m.next