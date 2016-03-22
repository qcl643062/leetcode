#coding=utf-8
"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        c = head
        a = []
        while True:
            if head != None:
                a.append(head.val)
                head = head.next
            else:
                break
        if len(a) - n == 0:
            return c.next
        if len(a) - n < 0:
            return c
        head1 = c
        for i in range(len(a) - n - 1):
            head1 = head1.next
        head1.next = head1.next.next
        return c
s = Solution()
ListNode1 = s.removeNthFromEnd(ListNode(0, ListNode(1, ListNode(0))), 1)
while ListNode1:
    print ListNode1.val
    ListNode1 = ListNode1.next
    